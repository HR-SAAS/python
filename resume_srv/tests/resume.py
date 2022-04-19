import json

import grpc

from resume_srv.model.model import Resume
from resume_srv.proto import resume_pb2, resume_pb2_grpc


class ResumeTest:
    def __init__(self, host, port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = resume_pb2_grpc.ResumeStub(channel)

    # def GetResumeDetail(self):
    #     res = self.stub.Resu(resume_pb2.GetResumeDetailRequest(id=1))
    #     print(res)

    def Create(self):
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
        return res.id

    def Update(self,id):
        res = self.stub.UpdateResume(
            resume_pb2.UpdateResumeRequest(id=id,user_id=2, name="测试简历", type=1, content="www.baidu.com", status=1))
        print(res)

    def Delete(self,id):
        res = self.stub.DeleteResume(resume_pb2.DeleteResumeRequest(id=id))
        print(res)

    def GetList(self):
        res = self.stub.GetResumeList(resume_pb2.GetResumeListRequest())
        print(res)

    def Get(self,id):
        res = self.stub.GetResumeDetail(resume_pb2.GetResumeDetailRequest(id=id))
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

