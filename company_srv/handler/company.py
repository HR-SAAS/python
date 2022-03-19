import google.protobuf.empty_pb2
import grpc

from company_srv.proto import company_pb2, company_pb2_grpc
from company_srv.model.model import Company

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
    if source.name:
        to.name = source.name
    if source.desc:
        to.desc = source.desc
    if source.website:
        to.website = source.website
    if source.config:
        to.config = source.config
    if source.tags:
        to.tags = source.tags
    if source.address:
        to.address = source.address
    if source.info:
        to.info = source.info
    if source.creator_id:
        to.creator_id = source.creator_id
    if source.parent_id:
        to.parent_id = source.parent_id
    if source.status:
        to.status = source.status
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
