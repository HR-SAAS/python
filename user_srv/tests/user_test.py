import grpc
from user_srv.proto import user_pb2, user_pb2_grpc


class UserTest:
    def __init__(self):
        channel = grpc.insecure_channel("192.168.50.1:2646")
        self.stub = user_pb2_grpc.UserStub(channel)

    def get_user_list(self):
        rsp: user_pb2.UserListResponse = self.stub.GetUserList(user_pb2.PageInfo(page=2, limit=10))
        print(rsp.total)
        for user in rsp.data:
            print(user)

    def find_user_by_id(self, id):
        rsp: user_pb2.UserListResponse = self.stub.FindUserById(user_pb2.IdRequest(id=id))
        print(rsp)
        return rsp

    def find_user_by_mobile(self, mobile):
        rsp: user_pb2.UserListResponse = self.stub.FindUserByMobile(user_pb2.MobileRequest(mobile=mobile))
        print(rsp)

    def create_user(self):
        rsp: user_pb2.UserListResponse = self.stub.CreateUser(
            user_pb2.UserRequest(mobile='12345678910', name='test', nick_name='test22'))

    def update_user(self):
        rsp: user_pb2.UserListResponse = self.stub.UpdateUser(
            user_pb2.UpdateUserRequest(id=1, mobile='12345678910', name='test', nick_name='test22'))

    def check_password(self,password,encrypt ):
        rsp: user_pb2.CheckPasswordResult = self.stub.CheckPassword(
            user_pb2.CheckPasswordRequest(password=password,encrypt = encrypt))
        return rsp

    def get_by_ids(self):
        req=user_pb2.GetUserListByIdsRequest(ids=[1,2,3,4])
        rsp:user_pb2.UserListResponse=self.stub.GetUserListByIds(req)
        for user in rsp.data:
            print(user)

if __name__ == '__main__':
    # test = UserTest()
    # # test.get_user_list()
    # test.create_user()
    # test.update_user()
    # r = test.find_user_by_id(1)
    from passlib.hash import pbkdf2_sha256
    #
    # print(None or 456)

    print(pbkdf2_sha256.verify('456',pbkdf2_sha256.hash('456')))
    # print(test.check_password('123456', r.password).result)
    # test.get_by_ids()
