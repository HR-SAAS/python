import grpc
from user_srv.proto import health_pb2_grpc, health_pb2


class HealthCheck:
    def __init__(self):
        channel = grpc.insecure_channel("192.168.159.119:5001")
        self.stub = health_pb2_grpc.HealthStub(channel)

    def check(self):
        rsp: health_pb2.HealthCheckResponse = self.stub.Check(health_pb2.HealthCheckRequest())
        print(rsp)

if __name__ == '__main__':
    test = HealthCheck()
    # test.get_user_list()
    r = test.check()
