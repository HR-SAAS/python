from user_srv.proto import user_pb2_grpc, user_pb2
from user_srv.model.model import User


class UserService(user_pb2_grpc.UserServicer):
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
            item = user_pb2.UserResponse()
            item.id = user.id
            item.mobile = user.mobile
            item.password = user.password
            if user.name:
                item.name = user.name
            if user.nick_name:
                item.nickName = user.nick_name
            rsp.data.append(item)

        return rsp
