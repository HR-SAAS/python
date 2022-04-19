import json

import grpc

from message_srv.model.model import UserMessage
from message_srv.proto import user_message_pb2, user_message_pb2_grpc


class UserMessageTest:
    def __init__(self, port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"192.168.50.1:{port}")
        self.stub = user_message_pb2_grpc.UserMessageStub(channel)

    def GetList(self):
        res = self.stub.GetMessageList(
            user_message_pb2.GetMessageListRequest(limit=1, search={"user_id": '1'}, sort={"created_at": "desc"}))
        print(res)

    # def GetResumeDetail(self):
    #     res = self.stub.Resu(resume_pb2.GetResumeDetailRequest(id=1))
    #     print(res)

    def Create(self):
        UserMessage()
        '''
        user_id = IntegerField(verbose_name="关联的用户id")
    
        source_type = CharField(verbose_name='来源模型: company/user/system')
        source_id = IntegerField(verbose_name='源id: ')
    
        relation_id=IntegerField(verbose_name='关联资源')
        relation_type=CharField(verbose_name='关联类型')
    
        type = CharField(verbose_name='消息类型')
        content = TextField(verbose_name='内容')
    
        is_read = BooleanField(verbose_name='已读?',default=False)
        status = EnumField(verbose_name='状态: 正常|删除|其他', default=1)
        '''
        res = self.stub.CreateMessage(
            user_message_pb2.CreateMessageRequest(user_id=2, content="测试消息", type="test", source_type="system",
                                                  source_id=1))
        print(res)
        return res.id

    def Update(self,id):
        res = self.stub.UpdateMessage(
            user_message_pb2.UpdateMessageRequest(id=id,type="asdasd", content="www.baidu.com", status=1,is_read=True))
        print(res)

    def Delete(self,id):
        res = self.stub.DeleteMessage(user_message_pb2.DeleteMessageRequest(id=id))
        print(res)


    def Get(self,id):
        res = self.stub.GetMessageDetail(user_message_pb2.GetMessageDetailRequest(id=id))
        print(res)


if __name__ == '__main__':
    test = UserMessageTest(8007)
    print("--------------create")
    id=test.Create()

    test.Get(id)

    print("--------------update")
    test.Update(id)
    print("--------------delete")
    test.Delete(id)
    test.GetList()
    test.Get(id)
