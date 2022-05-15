from common.model.ext import *

from recruit_srv.config import config


class BaseModel(BaseModel):
    class Meta:
        database = config.DB


# 岗位
class Post(BaseModel, DeletedModel):
    company_id = IntegerField(verbose_name='公司id')
    department_id = IntegerField(verbose_name='部门id,是否关联部门', default=0)
    creator_id = IntegerField(verbose_name='发布人')
    type = EnumField(verbose_name='类型id: 1普通招聘,2校招,3内推等', default=1)

    name = CharField(verbose_name='名称')
    desc = TextField(verbose_name='简介', null=True)
    content = TextField(verbose_name='内容')
    tags = JSONField(verbose_name='标签', null=True)

    experience = EnumField(verbose_name='经验:0不限,1:无经验 2: 一年 以此类推', default=0)
    education = EnumField(verbose_name='学历:0不限 1: 高中 2:大专 3:本科 4:研究生 5:其他', default=0)
    address = CharField(verbose_name='地址')

    # min_salary = IntegerField(verbose_name='工资范围')
    # max_salary = IntegerField(verbose_name='工资范围')

    view_count = IntegerField(verbose_name='浏览记录', default=0)
    like_count = IntegerField(verbose_name='收藏', default=0)

    start_at = TimestampField(verbose_name='开始时间')
    end_at = TimestampField(verbose_name='结束时间')
    status = EnumField(verbose_name='状态,3其他,2招满,1正常,0关闭', default=1)


#  投递记录,批量修改状态(短期内只能投递一次,避免重复投递)
class UserPost(BaseModel, DeletedModel):
    company_id = IntegerField(verbose_name='公司id,用于快速查询')
    post_id = IntegerField(verbose_name='岗位id')
    user_id = IntegerField(verbose_name='投递人id')
    resume_id = IntegerField(verbose_name='快照|简历id')
    resume_name = CharField(verbose_name='简历名称')
    resume_type = CharField(verbose_name='简历类型:')
    resume = TextField(verbose_name='简历内容:直接把对应的resume放入')
    remark = CharField(verbose_name='投递简历审核后的反馈')
    review_id = IntegerField(verbose_name='审核人')
    status = EnumField(verbose_name='投递状态: 未通过0,通过2,投递中:1', default=1)

# # 过了初筛，才有下一步流程，所以这里统一都是初筛流程，(目前:无需做过多的设计)
# class PostDataItem(Model):
#     pass


# # 企业招聘流程(咕咕)
# class PostProcess(Model):
#     company_id = IntegerField(verbose_name='企业id')
#
#
# #  简历模板咕咕(功能:让企业填充需要添加的字段)
# class Template(BaseModel):
#     pass
