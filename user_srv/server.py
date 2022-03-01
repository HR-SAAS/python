from concurrent import futures

import grpc

from user_srv.proto import user_pb2,user_pb2_grpc
from user_srv.handler.user import UserService


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserService(),server)
    server.add_insecure_port("[::]:5002")
    print(f"服务已经启动 localhost:5002")
    server.start()
    server.wait_for_termination()