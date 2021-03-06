import random

from peewee import *

from common.model.ext import EnumField
from user_srv.config import config


class BaseModel(Model):
    class Meta:
        database = config.DB


class User(BaseModel):
    SEX_ENUM = (
        (1, "男"),
        (0, "女")
    )
    mobile = CharField(max_length=11, index=True, verbose_name="电话号码")
    name = CharField(max_length=20, null=True, verbose_name="姓名")
    nick_name = CharField(max_length=255, null=True, verbose_name="昵称", column_name='nick_name')
    avatar = CharField(max_length=255, null=True, verbose_name="头像")
    sex = EnumField(verbose_name="性别", choices=SEX_ENUM)
    password = CharField(max_length=255, null=True, verbose_name="密码")
    group = IntegerField(verbose_name='权限组')
    current_role = EnumField(verbose_name='当前用户角色')
    status = EnumField(verbose_name='状态')


if __name__ == '__main__':
    config.DB.create_tables([User])

    # import hashlib
    # md5 = hashlib.md5()
    # md5.update(b'test')
    # print(md5.hexdigest())

    from passlib.hash import pbkdf2_sha256

    hash = pbkdf2_sha256.hash('123456')
    print(pbkdf2_sha256.verify('123456', hash))
    # print(hash)
    # print(pbkdf2_sha256.verify('123456',hash))
    # for i in range(19):
    #     user = User()
    #     user.name = f"{i}"
    #     user.sex = i%2
    #     user.password = pbkdf2_sha256.hash("123456")
    #     user.mobile = f"150700553{random.randint(1,10)}{i%10}"
    #     user.save()
