import grpc

from message_srv.model.model import UserMessage
from message_srv.proto import counter_pb2, counter_pb2_grpc


class CounterService(counter_pb2_grpc.ResumeCounterServiceServicer):

    def CountUserMessage(self, req: counter_pb2.CountUserMessageRequest, context):
        """-----------------------统计服务---
        统计一共多少个公司
        """
        model = UserMessage.select()
        if req.user_id:
            model = model.where(UserMessage.user_id == req.user_id)
        if req.search["content"]:
            model = model.where(UserMessage.content ** f"%{req.search['content']}%")
        # 类型获取,, 其他

        if req.status:
            model = model.where(UserMessage.status == req.status)
        rsp: counter_pb2.CountUserMessageResponse = counter_pb2.CountUserMessageResponse()
        rsp.count = model.count()
        return rsp
