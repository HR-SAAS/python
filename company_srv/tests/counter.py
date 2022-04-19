#  统计服务
import grpc

from company_srv.proto import counter_pb2_grpc,counter_pb2


class CountTest:
    def __init__(self, port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"192.168.50.1:{port}")
        self.stub = counter_pb2_grpc.CounterStub(channel)

    def CountCompany(self, search):
        """-----------------------统计服务---
        统计一共多少个公司
        """
        print(self.stub.CountCompany(counter_pb2.CountCompanyRequest(search=search)))

    def CountCompanyUser(self, search):
        """统计某公司多少人
        """
        print(self.stub.CountCompanyUser(counter_pb2.CountCompanyUserRequest(search=search)))


    def CountDepartment(self, search):
        """统计公司有多少个部门
        """
        print(self.stub.CountCompanyUser(counter_pb2.CountDepartmentRequest(search=search)))

    def CountDepartmentUser(self, search):
        """统计部门人数
        """
        print(self.stub.CountCompanyUser(counter_pb2.CountDepartmentUserRequest(search=search)))


if __name__ == '__main__':
    c = CountTest(8003)
    c.CountDepartment({"company_id":"1"})
    c.CountDepartment({})
    c.CountDepartmentUser({})
    c.CountCompanyUser({})
