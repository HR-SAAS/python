from datetime import datetime
from peewee import *
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


DB = ReconnectMysqlDatabase("hr-sass-company", host="120.79.71.33", port=3306,
                            user="hr-saas", password="pPYG7SGihSAS7zE5")


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated_at = DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        database = DB


class DeletedModel(Model):
    deleted_at = DateTimeField(default=None, verbose_name="删除时间", null=True)

    def save(self, *args, **kwargs):
        if self._pk is None:
            self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    @classmethod
    def delete(cls, permanently=False):
        if permanently:
            return super().delete()
        else:
            return super().update(deleted_at=datetime.now())

    def delete_instance(self, permanently=False, recursive=False, delete_nullable=False):
        if permanently:
            return self.delete().where(self._pk_expr()).execute()
        else:
            self.deleted_at = datetime.now()
            return self.save()

    @classmethod
    def select(cls, *fields):
        return super().select().where(cls.deleted_at == None)


class Company(BaseModel,DeletedModel):
    name = CharField(verbose_name='名称')
    desc = TextField(verbose_name='简介')
    website = CharField(verbose_name='官网')
    config = TextField(verbose_name='配置信息')
    creator_id = IntegerField(verbose_name='创建者,群主')
    parent_id = IntegerField(verbose_name='父id,子公司')
    status = BooleanField('状态')


class Department(BaseModel,DeletedModel):
    company_id = IntegerField(verbose_name='公司id')
    parent_id = IntegerField(verbose_name='父级id')
    icon = IntegerField(verbose_name='图标')
    name = CharField(verbose_name='名称')
    remark = CharField(verbose_name='备注')
    desc = TextField(verbose_name='简介')
    creator_id = IntegerField(verbose_name='负责人')
    status = BooleanField(verbose_name='状态')


# 用户企业表
class UserCompany(BaseModel,DeletedModel):
    user_id = IntegerField(verbose_name='用户id')
    company_id = IntegerField(verbose_name='公司id')
    department_id = IntegerField(verbose_name='部门id')
    status = BooleanField(verbose_name='状态,入职,离职,其他')


if __name__ == '__main__':
    #  打印
    DB.create_tables([Company])
    # c1=Company(name="test",desc="test",creator_id=1)
    # c1.save()
    # print()
    # c1 = Company().get(Company.id == 2)
    # c1.delete_instance()
    print(Company.select())
    for c in Company.select():
        print(c.id, c.name)
    # print(c1)
