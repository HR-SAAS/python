import google.protobuf.empty_pb2
import grpc

from user_srv.proto import user_pb2_grpc, user_pb2
from user_srv.model.model import User

from loguru import logger
from peewee import DoesNotExist


def user_convert_response(user):
    item = user_pb2.UserResponse()
    item.id = user.id
    return convert_user(user, item)


def response_convert_user(request):
    item = User()
    return convert_user(request, item)


def convert_user(source, to):
    # 手机号遮蔽
    for i in [
        "name",
        "mobile",
        "nick_name",
        "sex",
        "avatar",
        "current_role"
    ]:
        temp = getattr(source, i)
        if temp is not None:
            setattr(to, i, temp)
    return to


class UserService(user_pb2_grpc.UserServicer):
    @logger.catch
    def GetUserList(self, req: user_pb2.PageInfo, context):
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        stat = limit * (page - 1)

        users = User.select()
        rsp = user_pb2.UserListResponse()
        rsp.total = users.count()
        users = users.limit(limit).offset(stat)
        print(users)
        for user in users:
            rsp.data.append(user_convert_response(user))
        return rsp

    @logger.catch
    def FindUserByMobile(self, request, context):
        try:
            user = User.get(User.mobile == request.mobile)
            res = user_convert_response(user)
            res.password = user.password
            return res
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")

    @logger.catch
    def FindUserById(self, request, context):
        try:
            user = User.get(User.id == request.id)
            return user_convert_response(User.get(User.id == request.id))
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")

    @logger.catch
    def CreateUser(self, request: user_pb2.UserRequest, context):
        user = response_convert_user(request)
        from passlib.hash import pbkdf2_sha256
        user.password = pbkdf2_sha256.hash(request.password)
        user.save()
        return user_convert_response(user)

    @logger.catch
    def UpdateUser(self, request: user_pb2.UserRequest, context):
        user = User.get(User.id == request.id)
        user = convert_user(request, user)
        user.save()
        return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def CheckPassword(self, request: user_pb2.CheckPasswordRequest, context):
        try:
            from passlib.hash import pbkdf2_sha256
            return user_pb2.CheckPasswordResult(result=pbkdf2_sha256.verify(request.password, request.encrypt))
        except Exception as e:
            return user_pb2.CheckPasswordResult(result=False)

    @logger.catch
    def GetUserListByIds(self, request: user_pb2.GetUserListByIdsRequest, context):
        print(request.ids, type(request.ids))
        users = User.select().where(User.id.in_(list(request.ids)))
        rsp = user_pb2.UserListResponse()
        for user in users:
            rsp.data.append(user_convert_response(user))
        return rsp
