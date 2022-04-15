import google.protobuf.empty_pb2
import grpc

from resume_srv.proto import company_pb2, company_pb2_grpc, common_pb2
from resume_srv.model.model import Company, UserCompany

from loguru import logger
from peewee import DoesNotExist


def company_convert_response(company):
    item = company_pb2.CompanyResponse()
    item.id = company.id
    return convert_company(company, item)


def response_convert_company(request):
    item = Company()
    return convert_company(request, item)


def convert_company(source, to):
    for i in [
        "name",
        "desc",
        "website",
        "config",
        "tags",
        "address",
        "info",
        "creator_id",
        "parent_id",
        "status",
    ]:
        temp = getattr(source, i)
        if temp is not None and temp != -1 and temp != "":
            setattr(to, i, temp)
    return to


class ResumeService(company_pb2_grpc.CompanyServicer):

    @logger.catch
    def GetCompanyList(self, req: company_pb2.GetCompanyListRequest, context):
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        stat = limit * (page - 1)

        companies = Company.select()
        rsp = company_pb2.CompanyListResponse()
        rsp.total = companies.count()
        companies = companies.limit(limit).offset(stat)
        print(companies)
        for company in companies:
            rsp.data.append(company_convert_response(company))
        return rsp

    @logger.catch
    def GetCompanyDetail(self, req: company_pb2.GetCompanyDetailRequest, context):
        try:
            company = Company.get(Company.id == Company.id)
            return company_convert_response(company)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
            return company_pb2.CompanyResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
            return company_pb2.CompanyResponse()

    @logger.catch
    def CreateCompany(self, req: company_pb2.CreateCompanyRequest, context):
        from resume_srv.config.config import DB
        with DB.atomic() as transaction:
            try:
                company = response_convert_company(req)
                company.save()
                # 同时创建关联
                if company.creator_id:
                    UserCompany.create(
                        user_id=company.creator_id,
                        company_id=company.id,
                        status=1
                    )
                return company_convert_response(company)
            except Exception as e:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details("内部错误")
                return company_pb2.CompanyResponse()

    @logger.catch
    def UpdateCompany(self, req: company_pb2.UpdateCompanyRequest, context):
        try:
            company = Company.get_by_id(req.id)
            company = convert_company(req, company)
            company.save()
            return google.protobuf.empty_pb2.Empty()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
        finally:
            return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def DeleteCompany(self, req: company_pb2.DeleteCompanyRequest, context):
        try:
            Company.select().where(Company.id == req.id).get().delete_instance()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
        finally:
            return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def GetMyCompanyList(self, req: company_pb2.GetMyCompanyListRequest, context):
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        stat = limit * (page - 1)
        companyIds = UserCompany.select(UserCompany.company_id) \
            .where(UserCompany.user_id == req.user_id) \
            .limit(limit).offset(stat)
        # 获取全部id
        idList = []
        for i in companyIds:
            idList.append(i.company_id)
        companies = Company.select().where(Company.id in idList)
        rsp = company_pb2.CompanyListResponse()
        rsp.total = UserCompany.select(UserCompany.company_id) \
            .where(UserCompany.user_id == req.user_id) \
            .count()
        for company in companies:
            rsp.data.append(company_convert_response(company))
        return rsp

    @logger.catch
    def GetCompanyUserIdList(self, req, context):
        """公司下所有用户ID,分页
        """
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        stat = limit * (page - 1)
        userIds = UserCompany.select(UserCompany.user_id) \
            .where(UserCompany.company_id == req.company_id) \
            .limit(limit).offset(stat)
        total = UserCompany.select(UserCompany.user_id) \
            .where(UserCompany.company_id == req.company_id) \
            .count()
        rsp = common_pb2.UserIdList()
        rsp.total = total
        for uid in userIds:
            rsp.user_id.append(uid.user_id)
        return rsp

    @logger.catch
    def CreateUserCompany(self, req: company_pb2.SaveUserCompanyRequest, context):
        """加入公司
        """
        if UserCompany.select().where(UserCompany.company_id==req.company_id)\
                .where(UserCompany.user_id==req.user_id).count() >0:
            return google.protobuf.empty_pb2.Empty()
        if req.status == -1:
            req.status = 1
        UserCompany.create(user_id=req.user_id, company_id=req.company_id, status=req.status,info=req.info)
        return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def UpdateUserCompany(self, req: company_pb2.SaveUserCompanyRequest, context):
        """关系更新
        """
        userCompany = UserCompany.select().where(UserCompany.company_id == req.company_id) \
            .where(UserCompany.user_id == req.user_id).get()
        if req.info:
            userCompany.info = req.info
        if req.status != -1:
            userCompany.status = req.status
        userCompany.save()
        return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def DeleteUserCompany(self, req: company_pb2.DeleteUserCompanyRequest, context):
        """删除用户公司
        """
        try:
            item = UserCompany.select().where(UserCompany.user_id == req.user_id) \
                .where(UserCompany.company_id == req.company_id).get()
            item.delete_instance()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
        finally:
            return google.protobuf.empty_pb2.Empty()
