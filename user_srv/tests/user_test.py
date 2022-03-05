import grpc
from user_srv.proto import user_pb2, user_pb2_grpc


class UserTest:
    def __init__(self):
        channel = grpc.insecure_channel("localhost:5001")
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
            user_pb2.UserRequest(mobile='12345678910', name='test', nickName='test22'))

    def update_user(self):
        rsp: user_pb2.UserListResponse = self.stub.UpdateUser(
            user_pb2.UpdateUserRequest(id=1, mobile='12345678910', name='test', nickName='test22'))

    def check_password(self,password,encrypt ):
        rsp: user_pb2.CheckPasswordResult = self.stub.CheckPassword(
            user_pb2.CheckPasswordRequest(password=password,encrypt = encrypt))
        return rsp


if __name__ == '__main__':
    test = UserTest()
    # test.get_user_list()
    test.create_user()
    test.update_user()
    r = test.find_user_by_id(1)
    print(test.check_password('123456', r.password).result)
