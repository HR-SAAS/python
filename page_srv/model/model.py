from common.model.ext import *

from page_srv.config import config


class BaseModel(BaseModel):
    class Meta:
        database = config.DB


class Page(BaseModel, DeletedModel):
    company_id = IntegerField(verbose_name="关联的用户id")
    title = CharField(verbose_name='网页标题')
    data = JSONField(verbose_name='大json,页面数据')

class PageLog(BaseModel, DeletedModel):
    # 修改记录
    page_id = IntegerField(verbose_name='页面id')
    user_id = IntegerField(verbose_name='最后修改人')
    # 日志



if __name__ == '__main__':
    #  打印
    config.DB.create_tables([Page])

    # print(c1)
