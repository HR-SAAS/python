import os
import sys

BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASEDIR)

from message_srv.config import config
from message_srv.model.model import Resume


def init():
    config.DB.create_tables([Resume])


if __name__ == '__main__':
    print('开始初始化服务')
    init()
