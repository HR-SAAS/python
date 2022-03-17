from peewee import *


class BaseModel(Model):
    pass


class App(Model):
    name = CharField(verbose_name='名称')
    model_name = CharField(verbose_name='关联名称')
    app_key = CharField(verbose_name='应用密钥')


class Role(BaseModel):
    app_id = CharField(verbose_name='应用名称')
    name = CharField(verbose_name='角色名称')
    remark = CharField(verbose_name='备注')
    pass


class RolePermission(BaseModel):
    pass


class Permission(BaseModel):
    app_id = CharField(verbose_name='应用名称')
    name = CharField(verbose_name='权限名')
    remark = CharField(verbose_name='备注')
    pass


class UserPermission(BaseModel):
    pass
