import os
import sys

BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASEDIR)

from resume_srv.config import config
from resume_srv.model.model import Company, Department, UserCompany,UserDepartment


def init():
    config.DB.create_tables([Company, Department, UserCompany,UserDepartment])


if __name__ == '__main__':
    print('开始初始化服务')
    init()
