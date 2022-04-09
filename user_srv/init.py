import os
import sys

BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASEDIR)

from user_srv.config import config
from user_srv.model.model import User


def init():
    config.DB.create_tables([User])


if __name__ == '__main__':
    print('开始初始化服务')
    init()
