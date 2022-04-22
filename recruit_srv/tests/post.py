import json

import grpc

from recruit_srv.model.model import Post
from recruit_srv.proto import post_pb2, post_pb2_grpc


class ResumeTest:
    def __init__(self, host, port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = post_pb2_grpc.PostStub(channel)

    # def GetResumeDetail(self):
    #     res = self.stub.Resu(post_pb2.GetResumeDetailRequest(id=1))
    #     print(res)

    def Create(self):
        Post()
        '''
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

    view_count = IntegerField(verbose_name='浏览记录', default=0)
    like_count = IntegerField(verbose_name='收藏', default=0)

    start_at = TimestampField(verbose_name='开始时间')
    end_at = TimestampField(verbose_name='结束时间')
    status = EnumField(verbose_name='状态,3其他,2招满,1正常,0关闭', default=1)
        '''

        data = {
            'company_id': 1,
            'department_id': 2,
            'creator_id': 3,
            'type': 1,
            'name': "测试岗位",
            'desc': "简介",
            'content': "内容",
            'experience': 1,
            'education': 1,
            'address': "北京",
        }
        res = self.stub.CreatePost(
            post_pb2.CreatePostRequest(**data))
        print(res)
        return res.id

    def Update(self, id):
        data = {
            'id':id,
            'company_id': 1,
            'department_id': 2,
            'creator_id': 3,
            'type': 1,
            'name': "测试岗位",
            'desc': "简介",
            'content': "内容",
            'experience': 12,
            'education': 12,
            'address': "北京",
        }
        res = self.stub.UpdatePost(
            post_pb2.UpdatePostRequest(**data))
        print(res)

    def Delete(self, id):
        res = self.stub.DeletePost(post_pb2.DeletePostRequest(id=id))
        print(res)

    def GetList(self):
        res = self.stub.GetPostList(post_pb2.GetPostListRequest())
        print(res)

    def Get(self, id):
        res = self.stub.GetPostDetail(post_pb2.GetPostDetailRequest(id=id))
        print(res)


if __name__ == '__main__':
    test = ResumeTest('192.168.50.1', 8010)
    print("--------------create")
    id = test.Create()

    test.GetList()

    print("--------------update")
    test.Update(id)
    print("--------------delete")
    test.GetList()
    test.Get(id)
    test.Delete(id)
    test.Get(id)
