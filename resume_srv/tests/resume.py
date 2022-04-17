import json

import grpc

from resume_srv.model.model import Resume
from resume_srv.proto import resume_pb2, resume_pb2_grpc


class ResumeTest:
    def __init__(self, port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"192.168.50.1:{port}")
        self.stub = resume_pb2_grpc.ResumeStub(channel)

    def GetResumeList(self):
        res = self.stub.GetResumeList(resume_pb2.GetResumeListRequest(limit=1,search={"user_id":'1'},sort={"created_at":"desc"}))
        print(res)

    # def GetResumeDetail(self):
    #     res = self.stub.Resu(resume_pb2.GetResumeDetailRequest(id=1))
    #     print(res)

    def CreateResume(self):
        Resume()
        '''
        user_id = IntegerField(verbose_name="关联的用户id")
        name = CharField(verbose_name='简历名称')
        type = EnumField(verbose_name='类型: file,json,other')
        tag = JSONField(verbose_name='标签')
        content = TextField(verbose_name='内容|文件地址|等,其他')
        post_count = IntegerField(verbose_name='投递次数', default=0)
        status = EnumField(verbose_name='状态', default=1)
        '''
        res = self.stub.CreateResume(
            resume_pb2.CreateResumeRequest(user_id=1, name="测试简历", type=1, content="www.baidu.com", status=1))
        print(res)

    def UpdateResume(self):
        res = self.stub.UpdateResume(
            resume_pb2.UpdateResumeRequest(user_id=2, name="测试简历", type=1, content="www.baidu.com", status=1))
        print(res)

    def DeleteResume(self):
        res = self.stub.DeleteResume(resume_pb2.DeleteResumeRequest(id=6))
        print(res)

    def GetMyResumeList(self):
        res = self.stub.GetResumeList(resume_pb2.GetResumeListRequest())
        print(res)

    def GetResume(self):
        res = self.stub.GetResumeDetail(resume_pb2.GetResumeDetailRequest(id=1))
        print(res)

if __name__ == '__main__':
    test = ResumeTest(6801)
    print("--------------create")
    test.CreateResume()

    test.GetResumeList()

    print("--------------update")
    test.UpdateResume()
    print("--------------delete")
    # test.DeleteResume()
    test.GetResumeList()
    test.GetResume()