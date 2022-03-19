from common.model.ext import *

from company_srv.config import config


class BaseModel(BaseModel):
    class Meta:
        database = config.DB


class Company(BaseModel, DeletedModel):
    name = CharField(verbose_name='名称')
    desc = TextField(verbose_name='简介')
    website = CharField(verbose_name='官网', null=True)
    config = TextField(verbose_name='配置信息', null=True)
    tags = JSONField(verbose_name='标签', null=True)

    address = CharField(verbose_name='地址')
    info = JSONField(verbose_name='其他信息', null=True)

    creator_id = IntegerField(verbose_name='创建者,群主')
    parent_id = IntegerField(verbose_name='父id,子公司', default=0)
    status = EnumField(verbose_name='状态', default=1)


class Department(BaseModel, DeletedModel):
    company_id = IntegerField(verbose_name='公司id')
    parent_id = IntegerField(verbose_name='父级id')
    icon = IntegerField(verbose_name='图标', default=0)
    name = CharField(verbose_name='名称')
    remark = CharField(verbose_name='备注', null=True)
    desc = TextField(verbose_name='简介', null=True)

    info = JSONField(verbose_name='其他信息', null=True)
    creator_id = IntegerField(verbose_name='负责人')
    status = EnumField(verbose_name='状态', default=0)


# 用户企业表
class UserCompany(BaseModel, DeletedModel):
    user_id = IntegerField(verbose_name='用户id')
    company_id = IntegerField(verbose_name='公司id')
    department_id = IntegerField(verbose_name='部门id', default=0)
    # 别名
    remark = CharField(verbose_name='备注', null=True)
    info = JSONField(verbose_name='其他信息', null=True)
    status = EnumField(verbose_name='状态,入职,离职,其他')


class Post(BaseModel, DeletedModel):
    company_id = IntegerField(verbose_name='公司id')
    department_id = IntegerField(verbose_name='部门id', default=0)
    creator_id = IntegerField(verbose_name='发布人')
    type_id = IntegerField(verbose_name='类型id: 校招,直招,内推等', default=0)

    name = CharField(verbose_name='名称')
    desc = TextField(verbose_name='简介', null=True)
    content = TextField(verbose_name='内容')
    tags = JSONField(verbose_name='标签', null=True)

    experience = EnumField(verbose_name='经验,不限', default=0)
    education = EnumField(verbose_name='学历:二进制 0不限', default=0)
    address = CharField(verbose_name='地址')

    view_count = IntegerField(verbose_name='浏览记录', default=0)
    like_count = IntegerField(verbose_name='收藏', default=0)

    start_at = TimestampField(verbose_name='开始时间')
    end_at = TimestampField(verbose_name='结束时间')
    status = EnumField(verbose_name='状态,招满,正常,')


if __name__ == '__main__':
    #  打印
    config.DB.create_tables([Company, Department, UserCompany, Post])
    # c1=Company(name="test",desc="test",creator_id=1)
    # c1.save()
    # print()
    # c1 = Company().get(Company.id == 2)
    # c1.delete_instance()
    print(Company.select())
    for c in Company.select():
        print(c.id, c.name)
    # print(c1)
