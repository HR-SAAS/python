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
        user_id = IntegerField(verbose_name="关联的用户id")
        name = CharField(verbose_name='简历名称')
        type = EnumField(verbose_name='类型: file,json,other')
        tag = JSONField(verbose_name='标签')
        content = TextField(verbose_name='内容|文件地址|等,其他')
        post_count = IntegerField(verbose_name='投递次数', default=0)
        status = EnumField(verbose_name='状态', default=1)
        '''
        res = self.stub.CreatePost(
            post_pb2.CreatePostRequest(user_id=1, name="测试简历", type=1, content="www.baidu.com", status=1))
        print(res)
        return res.id

    def Update(self,id):
        res = self.stub.UpdatePost(
            post_pb2.UpdatePostRequest(id=id,user_id=2, name="测试简历", type=1, content="www.baidu.com", status=1))
        print(res)

    def Delete(self,id):
        res = self.stub.DeletePost(post_pb2.DeletePostRequest(id=id))
        print(res)

    def GetList(self):
        res = self.stub.GetPostList(post_pb2.GetPostListRequest())
        print(res)

    def Get(self,id):
        res = self.stub.GetPostDetail(post_pb2.GetPostDetailRequest(id=id))
        print(res)


if __name__ == '__main__':
    test = ResumeTest('192.168.50.1', 8008)
    print("--------------create")
    id=test.Create()

    test.GetList()

    print("--------------update")
    test.Update(id)
    print("--------------delete")
    test.GetList()
    test.Get(id)
    test.Delete(id)
    test.Get(id)

