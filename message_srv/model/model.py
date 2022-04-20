from common.model.ext import *

from message_srv.config import config


class BaseModel(BaseModel):
    class Meta:
        database = config.DB


# 你投递的某个流程：最新状态: xxxxx 点击此处区查看
class UserMessage(BaseModel, DeletedModel):
    user_id = IntegerField(verbose_name="关联的用户id")

    source_type = CharField(verbose_name='来源模型: company/user/system')
    source_id = IntegerField(verbose_name='源id: ')

    relation_id = IntegerField(verbose_name='关联资源')
    relation_type = CharField(verbose_name='关联类型')

    type = CharField(verbose_name='消息类型')
    content = TextField(verbose_name='内容')

    is_read = BooleanField(verbose_name='已读?', default=False)
    status = EnumField(verbose_name='状态: 正常|删除|其他', default=1)


if __name__ == '__main__':
    #  打印
    config.DB.create_tables([UserMessage])

    # print(c1)
