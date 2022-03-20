import google.protobuf.empty_pb2
import grpc

from company_srv.proto import company_pb2, company_pb2_grpc
from company_srv.model.model import Company, UserCompany

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
        if temp is not None:
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
        stat = limit * (page - 1)

        companies = Company.select()
        rsp = company_pb2.CompanyListResponse()
        rsp.total = companies.count()
        companies = companies.limit(limit).offset(stat)
        print(companies)
        for company in companies:
            rsp.data.append(company_convert_response(company))
        return rsp

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
        try:
            company = response_convert_company(req)
            company.save()
            return company_convert_response(company)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
            return company_pb2.CompanyResponse()

    def UpdateCompany(self, req: company_pb2.UpdateCompanyRequest, context):
        try:
            company = Company.get(Company.id == Company.id)
            company = convert_company(req, company)
            print(company)
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

    def DeleteCompany(self, request: company_pb2.DeleteCompanyRequest, context):
        try:
            company = Company.get(Company.id == Company.id)
            company.delete()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
        finally:
            return google.protobuf.empty_pb2.Empty()

    def GetMyCompanyList(self, req:company_pb2.GetMyCompanyListRequest, context):
        companyIds = UserCompany.select(UserCompany.company_id).get(UserCompany.user_id==req.user_id)
        # 获取全部id
        idList = []
        for i in companyIds:
            idList.append(i.company_id)
        companies = Company.where(Company.id in idList).select()
        print(companies)
        rsp = company_pb2.CompanyListResponse()
        rsp.total = companies.count()
        for company in companies:
            rsp.data.append(company_convert_response(company))
        return rsp