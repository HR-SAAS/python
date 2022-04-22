#  统计服务
import grpc

from recruit_srv.proto import counter_pb2_grpc, counter_pb2


class CountTest:
    def __init__(self,host, port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = counter_pb2_grpc.RecruitCounterServiceStub(channel)

    def CountPost(self, uid):
        """-----------------------统计服务---
        统计一共多少个公司
        """
        print(self.stub.CountPost(counter_pb2.CountPostRequest(company_id=0)).count)

    def CountUserPost(self):
        """-----------------------统计服务---
        统计一共多少个公司
        """
        print(self.stub.CountUserPost(counter_pb2.CountPostRequest()).count)

if __name__ == '__main__':
    c = CountTest('192.168.50.1',8010)
    c.CountPost(1)
    c.CountUserPost()
