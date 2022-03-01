from playhouse.pool import PooledMySQLDatabase  # 若长时间不使用则会断开
from playhouse.shortcuts import ReconnectMixin  # 自动重连


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    # python mro
    pass


MYSQL_DB = "hr-sass-user"
MYSQL_HOST = "120.79.71.33"
MYSQL_PORT = 3306
MYSQL_USERNAME = "hr-saas"
MYSQL_PASSWORD = "pPYG7SGihSAS7zE5"
DB = ReconnectMysqlDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USERNAME, password=MYSQL_PASSWORD)
