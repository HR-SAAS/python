import random

from peewee import *
from user_srv.config import database


class BaseModel(Model):
    class Meta:
        database = database.DB


class User(BaseModel):
    SEX_ENUM = (
        (1, "男"),
        (0, "女")
    )
    mobile = CharField(max_length=11, index=True, verbose_name="电话号码")
    name = CharField(max_length=20, null=True, verbose_name="姓名")
    nick_name = CharField(max_length=255, null=True, verbose_name="昵称")
    avatar = CharField(max_length=255, null=True, verbose_name="头像")
    sex = BooleanField(verbose_name="性别",choices=SEX_ENUM)
    password = CharField(max_length=255,null=True,verbose_name="密码")


if __name__ == '__main__':
    database.DB.create_tables([User])

    # import hashlib
    # md5 = hashlib.md5()
    # md5.update(b'test')
    # print(md5.hexdigest())

    from passlib.hash import pbkdf2_sha256
    hash = pbkdf2_sha256.hash('123456')
    # print(hash)
    # print(pbkdf2_sha256.verify('123456',hash))
    for i in range(19):
        user = User()
        user.name = f"{i}"
        user.sex = i%2
        user.password = pbkdf2_sha256.hash("123456")
        user.mobile = f"150700553{random.randint(1,10)}{i%10}"
        user.save()