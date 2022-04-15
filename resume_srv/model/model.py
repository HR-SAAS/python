from common.model.ext import *

from resume_srv.config import config


class BaseModel(BaseModel):
    class Meta:
        database = config.DB


class Resume(BaseModel, DeletedModel):
    user_id = IntegerField(verbose_name="关联的用户id")


if __name__ == '__main__':
    #  打印
    config.DB.create_tables([Resume])

    # print(c1)
