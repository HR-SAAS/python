import google.protobuf.empty_pb2
import grpc

from company_srv.proto import department_pb2, department_pb2_grpc
from company_srv.model.model import Department

from loguru import logger
from peewee import DoesNotExist


def department_convert_response(department):
    item = department_pb2.DepartmentResponse()
    item.id = department.id
    return convert_department(department, item)


def response_convert_department(request):
    item = Department()
    return convert_department(request, item)


def convert_department(source, to):
    if source.name:
        to.name = source.name
    return to


class DepartmentService(department_pb2_grpc.DepartmentServicer):

    @logger.catch
    def GetDepartmentList(self, req: department_pb2.GetDepartmentListRequest, context):
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        stat = limit * (page - 1)

        departments = Department.select()
        rsp = department_pb2.GetDepartmentListResponse()
        rsp.total = departments.count()
        departments = departments.limit(limit).offset(stat)
        print(departments)
        for department in departments:
            rsp.data.append(department_convert_response(department))
        return rsp

    def GetDepartmentDetail(self, req: department_pb2.GetDepartmentDetailRequest, context):
        try:
            company = Department.get(Department.id == req.id)
            return department_convert_response(company)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
            return department_pb2.DepartmentResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
            return department_pb2.DepartmentResponse()

    @logger.catch
    def CreateDepartment(self, req: department_pb2.CreateDepartmentRequest, context):
        try:
            # 开启事务
            item = response_convert_department(req)
            item.save()
            return department_convert_response(item)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
            return department_pb2.DepartmentResponse()

    def UpdateDepartment(self, req: department_pb2.UpdateDepartmentRequest, context):
        try:
            item = Department.get(Department.id == req.id)
            item = convert_department(req, item)
            print(item)
            item.save()
            return google.protobuf.empty_pb2.Empty()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
        finally:
            return google.protobuf.empty_pb2.Empty()

    def DeleteDepartment(self, req: department_pb2.DeleteDepartmentRequest, context):
        try:
            item = Department.get(Department.id == req.id)
            item.delete_instance()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
        finally:
            return google.protobuf.empty_pb2.Empty()

    def GetMyDepartmentList(self, request, context):
        """只需要判断creator_id是否相同,即可确定主要角色
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDepartmentUserIdList(self, request, context):
        """全部人员分页
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUserDepartment(self, request, context):
        """加入部门
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserDepartment(self, request, context):
        """人员部门表更新
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUserDepartment(self, request, context):
        """人员部门删除(软删除)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
