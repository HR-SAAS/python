from common.model.ext import *

from resume_srv.config import config


class BaseModel(BaseModel):
    class Meta:
        database = config.DB


class Resume(BaseModel, DeletedModel):
    user_id = IntegerField(verbose_name="关联的用户id")
    name = CharField(verbose_name='简历名称')
    type = EnumField(verbose_name='类型: file,json,other')
    status = EnumField(verbose_name='状态')
    tag = JSONField(verbose_name='标签')
    post_count = IntegerField(verbose_name='投递次数', default=0)
    content = TextField(verbose_name='内容')


if __name__ == '__main__':
    #  打印
    config.DB.create_tables([Resume])

    # print(c1)
