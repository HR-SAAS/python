import json

from loguru import logger
import nacos
from playhouse.pool import PooledMySQLDatabase  # 若长时间不使用则会断开
from playhouse.shortcuts import ReconnectMixin  # 自动重连


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    # python mro
    pass


NACOS_CONFIG = {
    "host": "localhost",
    "port": 8848,
    "namespace": "21b75e1f-3692-4268-82aa-42fbe83d0e7c",
    "username": "nacos",
    "password": "nacos",
    "dataId": "company-srv.json",
    "group": "dev"
}


def update_info(args):
    logger.info(f"配置信息变动:{args}")


client = nacos.NacosClient(f'{NACOS_CONFIG["host"]}:{NACOS_CONFIG["port"]}', namespace=NACOS_CONFIG["namespace"])

c = json.loads(client.get_config(NACOS_CONFIG["dataId"], NACOS_CONFIG["group"]))
logger.info(f"读取到配置信息:{c}")

SERVICE_REGISTER_HOST = c["consul"]["host"]
SERVICE_REGISTER_PORT = c["consul"]["port"]
SERVICE_NAME = c["name"]
SERVICE_ID = c["id"]
SERVICE_TAGS = c["tags"]

DB = ReconnectMysqlDatabase(c["mysql"]["database"], host=c["mysql"]["host"], port=c["mysql"]["port"],
                            user=c["mysql"]["user"], password=c["mysql"]["password"])
