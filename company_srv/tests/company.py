import grpc
from company_srv.proto import company_pb2, company_pb2_grpc


class CompanyTest:
    def __init__(self):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel("192.168.187.119:3529")
        self.stub = company_pb2_grpc.CompanyStub(channel)

    def get_user_list(self):
        rsp: company_pb2.CompanyListResponse = self.stub.GetCompanyList(company_pb2.GetCompanyListRequest(page=2, limit=10))
        print(rsp.total)
        for item in rsp.data:
            print(item)



if __name__ == '__main__':
    test = CompanyTest()
    test.get_user_list()

