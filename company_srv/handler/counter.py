import grpc

from company_srv.model.model import Company, UserCompany, UserDepartment, Department
from company_srv.proto import counter_pb2, counter_pb2_grpc


class CounterService(counter_pb2_grpc.CompanyCounterServicer):

    def CountCompany(self, req: counter_pb2.CountCompanyRequest, context):
        """-----------------------统计服务---
        统计一共多少个公司
        """
        model = Company().select()
        if req.search["creator_id"]:
            model = model.where(Company.creator_id == req.search["creator_id"])
        if req.search["name"]:
            model = model.where(Company.creator_id ** f"%{req.search['name']}%")
        if req.search["status"]:
            model = model.where(Company.status == req.status)
        rsp: counter_pb2.CompanyCountResponse = counter_pb2.CompanyCountResponse()
        rsp.count = model.count()
        return rsp

    def CountCompanyUser(self, req: counter_pb2.CountCompanyUserRequest, context):
        """统计某公司多少人
        """
        model = UserCompany().select()
        if req.search["company_id"]:
            model = model.where(UserCompany.company_id == req.search["company_id"])
        if req.search["user_id"]:
            model = model.where(UserCompany.user_id == req.search["user_id"])
        if req.search["status"]:
            model = model.where(UserCompany.status == req.status)
        rsp: counter_pb2.CompanyCountResponse = counter_pb2.CompanyCountResponse()
        rsp.count = model.count()
        return rsp

    def CountDepartment(self, req: counter_pb2.CountDepartmentRequest, context):
        """统计公司有多少个部门
        """
        model = Department().select()
        if req.search["creator_id"]:
            model = model.where(Department.creator_id == req.search["creator_id"])
        if req.search["company_id"]:
            model = model.where(Department.company_id == req.search["company_id"])
        if req.search["name"]:
            model = model.where(Department.creator_id ** f"%{req.search['name']}%")
        if req.search["status"]:
            model = model.where(Department.status == req.status)
        rsp: counter_pb2.CompanyCountResponse = counter_pb2.CompanyCountResponse()
        rsp.count = model.count()
        return rsp

    def CountDepartmentUser(self, req: counter_pb2.CountDepartmentUserRequest, context):
        """统计部门人数
        """
        model = UserDepartment().select()
        if req.search["department_id"]:
            model = model.where(UserDepartment.department_id == req.search["department_id"])
        if req.search["user_id"]:
            model = model.where(UserDepartment.user_id == req.search["user_id"])
        if req.search["status"]:
            model = model.where(UserDepartment.status == req.status)
        rsp: counter_pb2.CompanyCountResponse = counter_pb2.CompanyCountResponse()
        rsp.count = model.count()
        return rsp
