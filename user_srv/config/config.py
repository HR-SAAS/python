from playhouse.pool import PooledMySQLDatabase  # 若长时间不使用则会断开
from playhouse.shortcuts import ReconnectMixin  # 自动重连


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    # python mro
    pass

SERVICE_REGISTER_HOST = "localhost"
SERVICE_REGISTER_PORT = 9001
SERVICE_NAME = "user-srv"
SERVICE_ID = "user-srv"
SERVICE_TAGS = ["grpc", "python", "user"]

MYSQL_DB = "hr-sass-user"
MYSQL_HOST = "120.79.71.33"
MYSQL_PORT = 3306
MYSQL_USERNAME = "hr-saas"
MYSQL_PASSWORD = "pPYG7SGihSAS7zE5"
DB = ReconnectMysqlDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USERNAME, password=MYSQL_PASSWORD)
