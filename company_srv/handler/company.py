import time

import google.protobuf.empty_pb2
import google.protobuf.timestamp_pb2

import grpc

from company_srv.proto import company_pb2, company_pb2_grpc
from company_srv.model.model import Company, UserCompany

from loguru import logger
from peewee import DoesNotExist


def company_convert_response(company):
    item = company_pb2.CompanyResponse()
    item.id = company.id
    item.created_at.FromDatetime(company.created_at)
    item.updated_at.FromDatetime(company.updated_at)
    return convert_company(company, item)


def response_convert_company(request):
    item = Company()
    return convert_company(request, item)


def convert_company(source, to):
    if source.tags:
        to.tags = source.tags

    for i in [
        "name",
        "desc",
        "website",
        "config",
        "address",
        "info",
        "logo",
        "creator_id",
        "parent_id",
        "status",
    ]:
        temp = getattr(source, i)
        if temp is not None and temp != -1 and temp != "":
            setattr(to, i, temp)
    return to


class CompanyService(company_pb2_grpc.CompanyServicer):

    @logger.catch
    def GetCompanyList(self, req: company_pb2.GetCompanyListRequest, context):
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        start = limit * (page - 1)

        companies = Company.select()
        rsp = company_pb2.CompanyListResponse()
        rsp.total = companies.count()
        companies = companies.limit(limit).offset(start)
        print(companies)
        for company in companies:
            rsp.data.append(company_convert_response(company))
        return rsp

    @logger.catch
    def GetCompanyDetail(self, req: company_pb2.GetCompanyDetailRequest, context):
        try:
            company = Company.get(Company.id == req.id)
            return company_convert_response(company)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("???????????????")
            return company_pb2.CompanyResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"????????????")
            return company_pb2.CompanyResponse()

    @logger.catch
    def CreateCompany(self, req: company_pb2.CreateCompanyRequest, context):
        from company_srv.config.config import DB
        with DB.atomic() as transaction:
            try:
                company = response_convert_company(req)
                company.save()
                # ??????????????????
                if company.creator_id:
                    UserCompany.create(
                        user_id=company.creator_id,
                        company_id=company.id,
                        status=1
                    )
                return company_convert_response(company)
            except Exception as e:
                transaction.rollback()
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(f"????????????  {e}")
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
            context.set_details("???????????????")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("????????????")
        finally:
            return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def DeleteCompany(self, req: company_pb2.DeleteCompanyRequest, context):
        try:
            Company.select().where(Company.id == req.id).get().delete_instance()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("???????????????")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("????????????")
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
        start = limit * (page - 1)
        model = UserCompany.select(UserCompany.company_id) \
            .where(UserCompany.user_id == req.user_id)
        companyIds = model.limit(limit).offset(start)
        # ????????????id
        idList = []
        for i in companyIds:
            idList.append(i.company_id)
        companies = Company.select().where(Company.id << idList)
        rsp = company_pb2.CompanyListResponse()
        rsp.total = model.count()
        for company in companies:
            rsp.data.append(company_convert_response(company))
        return rsp

    @logger.catch
    def GetCompanyUserIdList(self, req, context):
        """?????????????????????ID,??????
        """
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        start = limit * (page - 1)
        model = UserCompany.select() \
            .where(UserCompany.company_id == req.company_id)

        data = model.limit(limit).offset(start)
        total = model.count()
        rsp = company_pb2.GetCompanyUserIdListResponse()
        rsp.total = total
        for item in data:
            temp = company_pb2.UserCompanyResponse(
                user_id=item.user_id, company_id=item.company_id,
                status=item.status, info=item.info,
                nick_name=item.nick_name, remark=item.remark,
            )
            temp.updated_at.FromDatetime(item.updated_at)
            temp.created_at.FromDatetime(item.created_at)
            rsp.data.append(temp)
        return rsp

    @logger.catch
    def CreateUserCompany(self, req: company_pb2.SaveUserCompanyRequest, context):
        """????????????
        """
        if UserCompany.select().where(UserCompany.company_id == req.company_id) \
                .where(UserCompany.user_id == req.user_id).count() > 0:
            return google.protobuf.empty_pb2.Empty()
        if req.status == -1:
            req.status = 1
        UserCompany.create(user_id=req.user_id, company_id=req.company_id, status=req.status, info=req.info)
        return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def UpdateUserCompany(self, req: company_pb2.SaveUserCompanyRequest, context):
        """????????????
        """
        logger.info(req)
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
        """??????????????????
        """
        try:
            item = UserCompany.select().where(UserCompany.user_id == req.user_id) \
                .where(UserCompany.company_id == req.company_id).get()
            item.delete_instance()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("???????????????")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("????????????")
        finally:
            return google.protobuf.empty_pb2.Empty()

    def GetCompanyListByIds(self, req: company_pb2.GetCompanyListByIdsRequest, context):
        """Missing associated documentation comment in .proto file."""
        data = Company.select().where(Company.id.in_(list(req.ids)))
        rsp = company_pb2.CompanyListResponse()
        for datum in data:
            rsp.data.append(company_convert_response(datum))
        return rsp
