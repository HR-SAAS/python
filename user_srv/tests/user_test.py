import grpc
from user_srv.proto import user_pb2,user_pb2_grpc


class UserTest:
    def __init__(self):
        channel =  grpc.insecure_channel("localhost:5002")
        self.stub = user_pb2_grpc.UserStub(channel)


    def get_user_list(self):
        rsp: user_pb2.UserListResponse= self.stub.GetUserList(user_pb2.PageInfo(page=2,limit=10))
        print(rsp.total)
        for user in rsp.data:
            print(user)

if __name__ == '__main__':
    test = UserTest()
    test.get_user_list()