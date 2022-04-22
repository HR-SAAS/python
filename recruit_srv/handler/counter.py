import grpc

from recruit_srv.model.model import Post, UserPost
from recruit_srv.proto import counter_pb2, counter_pb2_grpc


class CounterService(counter_pb2_grpc.RecruitCounterServiceServicer):

    def CountPost(self, req: counter_pb2.CountPostRequest, context):
        """统计岗位数
        """
        model = Post.select()

        if req.company_id:
            model.where(Post.company_id == req.company_id)

        if req.search is not None:
            search = req.search
            if search['company_id']:
                model = model.where(Post.company_id == search['company_id'])
            if search['name']:
                model = model.where(Post.name ** f"%{search['name']}%")
            if search['creator_id']:
                model = model.where(Post.creator_id == search['creator_id'])
            if search['start_at']:
                model = model.where(Post.start_at >= search['start_at'])
            if search['end_at']:
                model = model.where(Post.end_at <= search['end_at'])
        return counter_pb2.CountPostResponse(count=model.count())

    def CountUserPost(self, req: counter_pb2.CountUserPostRequest, context):
        """Missing associated documentation comment in .proto file."""
        model = UserPost.select()

        if req.search is not None:
            search = req.search
            if search['user_id']:
                model = model.where(UserPost.user_id == search['user_id'])
            if search['company_id']:
                model = model.where(UserPost.company_id == search['company_id'])
            if search['resume_id']:
                model = model.where(UserPost.resume_id == search['resume_id'])
            if search['status']:
                model = model.where(UserPost.status == search['status'])

        return counter_pb2.CountUserPostResponse(count=model.count())
