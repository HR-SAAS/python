from common.model.ext import *

from resume_srv.config import config


class BaseModel(BaseModel):
    class Meta:
        database = config.DB


class Resume(BaseModel, DeletedModel):
    user_id = IntegerField(verbose_name="关联的用户id")
    name = CharField(verbose_name='简历名称')
    type = CharField(verbose_name='类型: file,json,other')
    tag = JSONField(verbose_name='标签')
    content = TextField(verbose_name='内容|文件地址|等,其他')
    post_count = IntegerField(verbose_name='投递次数', default=0)
    status = EnumField(verbose_name='状态', default=1)


# 用户基本信息,用于企业筛选用户特征
class UserInfo(BaseModel):
    user_id = IntegerField(verbose_name='用户id')
    name = CharField(verbose_name='真实姓名')
    education = EnumField(verbose_name='学历')
    role = EnumField(verbose_name='当前角色: 1.应届生 2. 工作者')
    # 到岗时间等


# 期望信息(用户希望找一个什么样的工作,计划于: 用户投递中心=>批量投递等功能)
class WantInfo(BaseModel, DeletedModel):
    post = CharField(verbose_name='期望岗位')
    address = CharField(verbose_name='期望地址')
    expr = EnumField(verbose_name='经验状态')


if __name__ == '__main__':
    #  打印
    config.DB.create_tables([Resume])

    # print(c1)
