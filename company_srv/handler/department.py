import google.protobuf.empty_pb2
import grpc

from company_srv.proto import department_pb2, department_pb2_grpc
from company_srv.model.model import Department, UserDepartment

from loguru import logger
from peewee import DoesNotExist


def department_convert_response(department):
    item = department_pb2.DepartmentResponse()
    item.id = department.id
    item.created_at.FromDatetime(department.created_at)
    item.updated_at.FromDatetime(department.updated_at)
    return convert_department(department, item)


def response_convert_department(request):
    item = Department()
    return convert_department(request, item)


def convert_department(source, to):
    for i in [
        "company_id",
        "parent_id",
        "icon",
        "name",
        "remark",
        "desc",
        "size",
        "info",
        "creator_id",
        "status",
    ]:
        temp = getattr(source, i)
        if temp is not None and temp != -1 and temp != "":
            setattr(to, i, temp)
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
        from company_srv.config.config import DB
        with DB.atomic() as transaction:
            try:
                # 开启事务
                item = response_convert_department(req)
                item.save()
                return department_convert_response(item)
            except Exception as e:
                transaction.rollback()
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details("内部错误")
                return department_pb2.DepartmentResponse()

    @logger.catch
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

    @logger.catch
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

    @logger.catch
    def GetMyDepartmentList(self, req: department_pb2.GetMyDepartmentListRequest, context):
        """只需要判断creator_id是否相同,即可确定主要角色
        """
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        stat = limit * (page - 1)
        model = UserDepartment.select(UserDepartment.department_id) \
            .where(UserDepartment.user_id == req.user_id)
        companyIds = model.limit(limit).offset(stat)
        # 获取全部id
        idList = []
        for i in companyIds:
            idList.append(i.department_id)
        departments = Department.select().where(Department.id << idList)
        rsp = department_pb2.GetDepartmentListResponse()
        rsp.total = model.count()
        for departments in departments:
            rsp.data.append(department_convert_response(departments))
        return rsp

    @logger.catch
    def GetDepartmentUserIdList(self, req: department_pb2.GetDepartmentUserListRequest, context):
        """全部人员分页
        """
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        stat = limit * (page - 1)
        model = UserDepartment.select() \
            .where(UserDepartment.department_id == req.department_id)

        data = model.limit(limit).offset(stat)
        total = model.count()

        rsp = department_pb2.GetDepartmentUserIdListResponse()
        rsp.total = total
        for item in data:
            rsp.data.append(
                department_pb2.UserDepartmentResponse(
                    user_id=item.user_id,department_id=item.department_id,
                    status=item.status,nick_name=item.nick_name,
                    remark=item.remark
                )
            )
        return rsp

    @logger.catch
    def CreateUserDepartment(self, req: department_pb2.SaveUserDepartmentRequest, context):
        """加入部门
        """
        if UserDepartment.select(). \
                where(UserDepartment.department_id == req.department_id) \
                .where(UserDepartment.user_id == req.user_id).count() > 0:
            return google.protobuf.empty_pb2.Empty()
        if req.status == -1:
            req.status = 1
        UserDepartment.create(user_id=req.user_id, department_id=req.department_id, status=req.status)
        return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def UpdateUserDepartment(self, req: department_pb2.SaveUserDepartmentRequest, context):
        """人员部门表更新
        """
        try:
            item = UserDepartment.select().where(UserDepartment.department_id == req.department_id) \
                .where(UserDepartment.user_id == req.user_id).get()
            if req.status != -1:
                item.status = req.status
            item.save()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
        finally:
            return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def DeleteUserDepartment(self, req: department_pb2.DeleteUserDepartmentRequest, context):
        """人员部门删除(软删除)
        """
        try:
            item = UserDepartment.select().where(UserDepartment.user_id == req.user_id) \
                .where(UserDepartment.department_id == req.department_id).get()
            item.delete_instance()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
        finally:
            return google.protobuf.empty_pb2.Empty()
