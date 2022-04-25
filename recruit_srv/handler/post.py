import json

import google.protobuf.empty_pb2
import grpc

from recruit_srv.proto import post_pb2, post_pb2_grpc
from recruit_srv.model.model import Post

from loguru import logger
from peewee import DoesNotExist


def post_convert_response(post):
    item = post_pb2.PostResponse()
    if post is None:
        return item
    item.id = post.id
    # 简历信息设置
    item.start_at.FromDatetime(post.start_at)
    item.end_at.FromDatetime(post.end_at)

    item.created_at.FromDatetime(post.created_at)
    item.updated_at.FromDatetime(post.updated_at)
    return convert_post(post, item)


def response_convert_post(request):
    item = Post()
    #  写入时间
    if request.start_at.seconds:
        item.start_at = request.start_at.ToDatetime()
    if request.end_at.seconds:
        item.end_at = request.end_at.ToDatetime()
    return convert_post(request, item)


def convert_post(source, to):
    for i in [
        "company_id",
        "department_id",
        "creator_id",
        "type",
        "name",
        "desc",
        "content",
        "experience",
        "education",
        "address",
        "status"
    ]:
        temp = getattr(source, i)
        if temp is not None and temp != -1 and temp != "":
            setattr(to, i, temp)
    return to


class PostService(post_pb2_grpc.PostServicer):

    @logger.catch
    def GetPostList(self, req: post_pb2.GetPostListRequest, context):
        """获取列表
        """
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        start = limit * (page - 1)
        model = Post.select()

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

        if req.sort is not None:
            for i, v in dict(req.sort).items():
                model = model.order_by(i, v)
        # 动态search
        rsp = post_pb2.PostListResponse()

        rsp.total = model.count()
        data = model.limit(limit).offset(start)
        print(data)
        for item in data:
            rsp.data.append(post_convert_response(item))
        return rsp

    @logger.catch
    def CreatePost(self, req: post_pb2.CreatePostRequest, context):
        """创建
        """
        post = response_convert_post(req)
        post.save()
        return post_convert_response(post)

    @logger.catch
    def UpdatePost(self, req: post_pb2.UpdatePostRequest, context):
        """更新
        """
        from recruit_srv.config.config import DB
        with DB.atomic() as transaction:
            try:
                item = Post.get_by_id(req.id)
                item = convert_post(req, item)
                if req.start_at.seconds:
                    item.start_at = req.start_at.ToDatetime()
                if req.end_at.seconds:
                    item.end_at = req.end_at.ToDatetime()
                item.save()
                return post_convert_response(item)
            except Exception as e:
                transaction.rollback()
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(f"内部错误  {e}")
                return post_pb2.PostResponse()

    @logger.catch
    def DeletePost(self, req: post_pb2.DeletePostRequest, context):
        """删除
        """
        try:
            item = Post.get_by_id(req.id)
            item.delete_instance()
            return google.protobuf.empty_pb2.Empty()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("内部错误")
        finally:
            return google.protobuf.empty_pb2.Empty()

    @logger.catch
    def GetPostDetail(self, req: post_pb2.GetPostDetailRequest, context):
        """详情
        """
        try:
            item = Post.get_by_id(req.id)
            return post_convert_response(item)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
            return post_convert_response(None)

    def GetPostListByIds(self, req:post_pb2.GetPostListByIdsRequest, context):
        """根据id获取数据
        """
        data = Post.select().where(Post.id << list(req.ids))
        res = post_pb2.PostListResponse()
        for datum in data:
            res.data.append(post_convert_response(datum))

        return res

