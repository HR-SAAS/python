import json
import os

from loguru import logger
import nacos
from playhouse.pool import PooledMySQLDatabase  # 若长时间不使用则会断开
from playhouse.shortcuts import ReconnectMixin  # 自动重连


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    # python mro
    pass


NACOS_CONFIG = {
    "host": os.getenv('NACOS_HOST', 'localhost'),
    "port": int(os.getenv('NACOS_PORT', '8848')),
    "namespace": os.getenv('NACOS_NAMESPACE', '9d43da2e-bed0-4dec-8ee7-3f83c7254192'),
    "username": os.getenv('NACOS_USERNAME', 'nacos'),
    "password": os.getenv('NACOS_PASSWORD', 'nacos'),
    "dataId": os.getenv('NACOS_DATA_ID', 'recruit-srv.json'),
    "group": os.getenv('NACOS_GROUP', 'dev')
}


def update_info(args):
    logger.info(f"配置信息变动:{args}")


client = nacos.NacosClient(f'{NACOS_CONFIG["host"]}:{NACOS_CONFIG["port"]}', namespace=NACOS_CONFIG["namespace"],
                           username=NACOS_CONFIG['username'], password=NACOS_CONFIG['password'])

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
