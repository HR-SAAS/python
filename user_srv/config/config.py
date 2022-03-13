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
    "namespace": "92eb12b0-1a27-41ec-a6f8-4a8bb1611e56",
    "username": "nacos",
    "password": "nacos",
    "dataId": "user-srv.json",
    "group": "dev"
}


def update_info(args):
    logger.info(f"配置信息变动:{args}")


client = nacos.NacosClient(f'{NACOS_CONFIG["host"]}:{NACOS_CONFIG["port"]}', namespace=NACOS_CONFIG["namespace"])

c = json.loads(client.get_config(NACOS_CONFIG["dataId"], NACOS_CONFIG["group"]))

# SERVICE_REGISTER_HOST = "localhost"
# SERVICE_REGISTER_PORT = 9001
# SERVICE_NAME = "user-srv"
# SERVICE_ID = "user-srv"
# SERVICE_TAGS = ["grpc", "python", "user"]


SERVICE_REGISTER_HOST = c["consul"]["host"]
SERVICE_REGISTER_PORT = c["consul"]["port"]
SERVICE_NAME = c["name"]
SERVICE_ID = c["id"]
SERVICE_TAGS = c["tags"]

# MYSQL_DB = "hr-sass-user"
# MYSQL_HOST = "120.79.71.33"
# MYSQL_PORT = 3306
# MYSQL_USERNAME = "hr-saas"
DB = ReconnectMysqlDatabase(c["mysql"]["database"], host=c["mysql"]["host"], port=c["mysql"]["port"],
                            user=c["mysql"]["user"], password=c["mysql"]["password"])
