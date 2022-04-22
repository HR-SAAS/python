import os
import sys

BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASEDIR)

from recruit_srv.config import config
from recruit_srv.model.model import Post, UserPost


def init():
    config.DB.create_tables([Post, UserPost])


if __name__ == '__main__':
    print('开始初始化服务')
    init()
