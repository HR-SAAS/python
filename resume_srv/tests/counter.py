#  统计服务
import grpc

from resume_srv.proto import counter_pb2_grpc, counter_pb2


class CountTest:
    def __init__(self, port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"192.168.50.1:{port}")
        self.stub = counter_pb2_grpc.ResumeCounterServiceStub(channel)

    def CountUserMessage(self, uid):
        """-----------------------统计服务---
        统计一共多少个公司
        """
        print(self.stub.CountResume(counter_pb2.CountResumeRequest(user_id=uid,status=-1,type=-1)))


if __name__ == '__main__':
    c = CountTest(8008)
    c.CountUserMessage(1)
