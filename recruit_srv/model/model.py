from common.model.ext import *

# 岗位
class Post(BaseModel, DeletedModel):
    company_id = IntegerField(verbose_name='公司id')
    department_id = IntegerField(verbose_name='部门id', default=0)
    creator_id = IntegerField(verbose_name='发布人')
    type_id = EnumField(verbose_name='类型id: 校招,直招,内推等', default=0)

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
    status = EnumField(verbose_name='状态,招满,正常,关闭')


#  模板
class Template(BaseModel):
    pass


#  投递记录
class PostData(BaseModel):
    pass


# 招聘流程
class PostProcess(Model):
    pass


# 招聘流程日志
class PostProcessLog(Model):
    pass


# 招聘简历任务子项目
class PostProcessLogItem(Model):
    pass
