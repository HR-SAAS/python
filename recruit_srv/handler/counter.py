import grpc

from recruit_srv.model.model import Post, UserPost
from recruit_srv.proto import counter_pb2, counter_pb2_grpc


class CounterService(counter_pb2_grpc.RecruitCounterServiceServicer):

    def CountPost(self, request, context):
        """统计岗位数
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CountUserPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
