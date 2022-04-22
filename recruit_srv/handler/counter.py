import grpc

from recruit_srv.model.model import Resume
from recruit_srv.proto import counter_pb2, counter_pb2_grpc


class CounterService(counter_pb2_grpc.ResumeCounterServiceServicer):

    def CountResume(self, req: counter_pb2.CountResumeRequest, context):
        """-----------------------统计服务---
        """
        # user_id
        # name
        # type
        # status
        model = Resume.select()
        if req.user_id>-1:
            model = model.where(Resume.user_id == req.user_id)
        if req.type > -1:
            model = model.where(Resume.type == req.user_id)
        if req.name:
            model = model.where(Resume.name ** f"%{req.name}%")
        # 类型获取,, 其他
        if req.status > -1:
            model = model.where(Resume.status == req.status)
        rsp: counter_pb2.CountResumeResponse = counter_pb2.CountResumeResponse()
        rsp.count = model.count()
        return rsp
