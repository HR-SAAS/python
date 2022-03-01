import argparse
import os.path
import signal
import sys
from concurrent import futures

import grpc

# 配置引入路径
BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASEDIR)
from user_srv.proto import user_pb2, user_pb2_grpc
from user_srv.handler.user import UserService
from loguru import logger


def on_exit(signum, frame):
    logger.warning('进程中断')
    sys.exit(0)


if __name__ == '__main__':
    logger.add("logs/user_srv_{time}.log")

    argument = argparse.ArgumentParser()
    argument.add_argument('--port',nargs='?',type=int,default=5002,help='listen port')
    argument.add_argument('--host',nargs='?',type=str,default='127.0.0.1',help='listen host')
    args = argument.parse_args()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserService(), server)
    server.add_insecure_port(f"{args.host}:{args.port}")

    signal.signal(signal.SIGINT, on_exit)
    signal.signal(signal.SIGTERM, on_exit)

    logger.info(f"服务已经启动 {args.host}:{args.port}")
    server.start()
    server.wait_for_termination()
