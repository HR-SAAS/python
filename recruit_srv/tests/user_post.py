import json

import grpc

from recruit_srv.model.model import UserPost
from recruit_srv.proto import user_post_pb2, user_post_pb2_grpc


class UserPostTest:
    def __init__(self, host, port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = user_post_pb2_grpc.UserPostStub(channel)

    # def GetResumeDetail(self):
    #     res = self.stub.Resu(user_post_pb2.GetResumeDetailRequest(id=1))
    #     print(res)

    def Create(self):
        UserPost()
        '''
    company_id = IntegerField(verbose_name='公司id,用于快速查询')
    post_id = IntegerField(verbose_name='岗位id')
    user_id = IntegerField(verbose_name='投递人id')
    resume_id = IntegerField(verbose_name='简历id')
    resume_type = CharField(verbose_name='简历类型:')
    resume = TextField(verbose_name='简历内容:直接把对应的resume放入')
    remark = CharField(verbose_name='投递简历审核后的反馈')
    review_id = IntegerField(verbose_name='审核人')
    status = EnumField(verbose_name='投递状态: 未通过0,通过2,投递中:1', default=1)
        '''

        data = {
            'company_id': 1,
            'post_id': 2,
            'user_id': 3,
            'resume_id': 1,
            'resume_type': "text",
            'resume': "简历",
            'remark': "备注",
            'review_id': 1,
            'status': 1,
        }
        res = self.stub.CreateUserPost(
            user_post_pb2.CreateUserPostRequest(**data))
        print(res)
        return res.id

    def Update(self, id):
        data = {
            'id':id,
            'company_id': 1,
            'post_id': 2,
            'user_id': 3,
            'resume_id': 1,
            'resume_type': "text",
            'resume': "简历1",
            'remark': "备注2",
            'review_id': 1,
            'status': 1,
        }
        res = self.stub.UpdateUserPost(
            user_post_pb2.UpdateUserPostRequest(**data))
        print(res)

    def Delete(self, id):
        res = self.stub.DeleteUserPost(user_post_pb2.DeleteUserPostRequest(id=id))
        print(res)

    def GetList(self):
        res = self.stub.GetUserPostList(user_post_pb2.GetUserPostListRequest())
        print(res)

    def Get(self, id):
        res = self.stub.GetUserPostDetail(user_post_pb2.GetUserPostDetailRequest(id=id))
        print(res)


if __name__ == '__main__':
    test = UserPostTest('192.168.50.1', 8010)
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
