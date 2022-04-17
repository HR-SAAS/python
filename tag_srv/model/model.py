from common.model.ext import *

from tag_srv.config import config


class BaseModel(BaseModel):
    class Meta:
        database = config.DB


class Tag(BaseModel, DeletedModel):
    type = CharField(verbose_name="关联的模型")
    type_id = CharField(verbose_name='类型ID')
    name = CharField(verbose_name='简历名称')
    status = EnumField(verbose_name='状态', default=1)


if __name__ == '__main__':
    #  打印
    config.DB.create_tables([Tag])

    # print(c1)
