from common.model.ext import *

from message_srv.config import config


class BaseModel(BaseModel):
    class Meta:
        database = config.DB


class UserMessage(BaseModel, DeletedModel):
    user_id = IntegerField(verbose_name="关联的用户id")
    source_type = CharField(verbose_name='源模型')
    source_id = IntegerField(verbose_name='源id')

    type = CharField(verbose_name='类型')
    content = TextField(verbose_name='内容')

    is_read = BooleanField(verbose_name='已读?')
    status = EnumField(verbose_name='状态: 正常|删除|其他', default=1)


if __name__ == '__main__':
    #  打印
    config.DB.create_tables([UserMessage])

    # print(c1)
