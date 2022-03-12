import argparse
import os.path
import signal
import socket
import sys
from concurrent import futures

import grpc

# 配置引入路径
from common.register.consul import ConsulRegister

BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASEDIR)
from user_srv.proto import user_pb2, user_pb2_grpc
from common.health_check.proto import health_pb2_grpc
from user_srv.handler.user import UserService
from common.health_check.handler.health import HealthService
from loguru import logger
from user_srv.config import base


def on_exit(signum, frame):
    logger.warning('进程中断')
    sys.exit(0)

def get_free_tcp_port():
    # 获取
    tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp.bind(("",0))
    _,port = tcp.getsockname()
    tcp.close()
    return port

if __name__ == '__main__':
    logger.add("logs/user_srv_{time}.log", rotation='1day')

    argument = argparse.ArgumentParser()
    argument.add_argument('--port', nargs='?', type=int, default=0, help='listen port')
    argument.add_argument('--host', nargs='?', type=str, default='192.168.205.119', help='listen host')
    args = argument.parse_args()

    if args.port:
        port = args.port
    else:
        port = get_free_tcp_port()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserService(), server)
    health_pb2_grpc.add_HealthServicer_to_server(HealthService(), server)
    server.add_insecure_port(f"{args.host}:{port}")
    c = ConsulRegister(base.SERVICE_REGISTER_HOST,base.SERVICE_REGISTER_PORT)

    logger.info(f"开始注册服务")
    register_res = c.register(base.SERVICE_NAME,base.SERVICE_ID,args.host,port,base.SERVICE_TAGS)
    if register_res:
        logger.info("服务注册成功")
    else:
        logger.error("服务注册失败")
        exit(-1)

    signal.signal(signal.SIGINT, on_exit)
    signal.signal(signal.SIGTERM, on_exit)

    logger.info(f"服务已经启动 {args.host}:{port}")
    server.start()
    server.wait_for_termination()
