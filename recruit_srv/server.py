import argparse
import os.path
import signal
import sys
from concurrent import futures
from functools import partial
import grpc



BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASEDIR)

# 配置引入路径
from common.utils import get_free_tcp_port, get_ip_addr
from recruit_srv.handler.counter import CounterService
from recruit_srv.proto import post_pb2_grpc,user_post_pb2_grpc
from common.health_check.proto import health_pb2_grpc
from common.register.consul import ConsulRegister
from recruit_srv.handler.post import PostService
from recruit_srv.handler.user_post import UserPostService
from common.health_check.handler.health import HealthService
from loguru import logger
from recruit_srv.config import config


def on_exit(signum, frame, service_id):
    c = ConsulRegister(config.SERVICE_REGISTER_HOST, config.SERVICE_REGISTER_PORT)
    logger.info(f"开始注销服务")
    deregister_res = c.deregister(service_id)
    if deregister_res:
        logger.info("服务注销成功")
    else:
        logger.error("服务注销失败")
    logger.warning('进程中断')
    sys.exit(0)


if __name__ == '__main__':

    logger.add("logs/recruit_srv_{time}.log", rotation='1day')

    argument = argparse.ArgumentParser()
    argument.add_argument('--port', nargs='?', type=int, default=0, help='listen port')
    argument.add_argument('--host', nargs='?', type=str, default=0, help='listen host')
    args = argument.parse_args()

    if args.port:
        port = args.port
    else:
        port = get_free_tcp_port()

    if args.host:
        host = args.host
    else:
        host = get_ip_addr()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 招聘服务
    post_pb2_grpc.add_PostServicer_to_server(PostService(), server)
    user_post_pb2_grpc.add_UserPostServicer_to_server(UserPostService(),server)
    # 统计服务


    # 健康
    health_pb2_grpc.add_HealthServicer_to_server(HealthService(), server)
    server.add_insecure_port(f"{host}:{port}")
    c = ConsulRegister(config.SERVICE_REGISTER_HOST, config.SERVICE_REGISTER_PORT)

    import uuid

    server_id = str(uuid.uuid1())
    logger.info(f"开始注册服务")
    register_res = c.register(config.SERVICE_NAME, server_id, host, port, config.SERVICE_TAGS)
    if register_res:
        logger.info("服务注册成功")
    else:
        logger.error("服务注册失败")
        exit(-1)

    signal.signal(signal.SIGINT, partial(on_exit, service_id=server_id))
    signal.signal(signal.SIGTERM, partial(on_exit, service_id=server_id))

    logger.info(f"服务已经启动 {host}:{port}")

    config.client.add_config_watcher(config.NACOS_CONFIG["dataId"], config.NACOS_CONFIG["group"], config.update_info)

    server.start()
    server.wait_for_termination()
