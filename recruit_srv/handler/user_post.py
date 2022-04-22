import json

import google.protobuf.empty_pb2
import grpc

from recruit_srv.proto import user_post_pb2, user_post_pb2_grpc
from recruit_srv.model.model import UserPost

from loguru import logger
from peewee import DoesNotExist


def user_post_convert_response(user_post):
    item = user_post_pb2.UserPostResponse()
    if user_post is None:
        return item
    item.id = user_post.id

    item.created_at.FromDatetime(user_post.created_at)
    item.updated_at.FromDatetime(user_post.updated_at)
    return convert_user_post(user_post, item)


def response_convert_user_post(request):
    item = UserPost()
    #  写入时间
    return convert_user_post(request, item)


def convert_user_post(source, to):
    for i in [
        "company_id",
        "post_id",
        "user_id",
        "resume_id",
        "resume",
        "remark",
        "review_id",
        "status",
    ]:
        temp = getattr(source, i)
        if temp is not None and temp != -1 and temp != "":
            setattr(to, i, temp)
    return to


class UserPostService(user_post_pb2_grpc.UserPostServicer):

    @logger.catch
    def GetUserPostList(self, req: user_post_pb2.GetUserPostListRequest, context):
        """获取列表
        """
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        start = limit * (page - 1)
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

        if req.sort is not None:
            for i, v in dict(req.sort).items():
                model = model.order_by(i, v)
        # 动态search
        rsp = user_post_pb2.UserPostListResponse()

        rsp.total = model.count()
        data = model.limit(limit).offset(start)
        print(data)
        for item in data:
            rsp.data.append(user_post_convert_response(item))
        return rsp

    @logger.catch
    def CreateUserPost(self, req: user_post_pb2.CreateUserPostRequest, context):
        """创建
        """
        user_post = response_convert_user_post(req)
        user_post.save()
        return user_post_convert_response(user_post)

    @logger.catch
    def UpdateUserPost(self, req: user_post_pb2.UpdateUserPostRequest, context):
        """更新
        """
        from recruit_srv.config.config import DB
        with DB.atomic() as transaction:
            try:
                item = UserPost.get_by_id(req.id)
                item = convert_user_post(req, item)
                item.save()
                return user_post_convert_response(item)
            except Exception as e:
                transaction.rollback()
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(f"内部错误  {e}")
                return user_post_pb2.UserPostResponse()

    @logger.catch
    def DeleteUserPost(self, req: user_post_pb2.DeleteUserPostRequest, context):
        """删除
        """
        try:
            item = UserPost.get_by_id(req.id)
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
    def GetUserPostDetail(self, req: user_post_pb2.GetUserPostDetailRequest, context):
        """详情
        """
        try:
            item = UserPost.get_by_id(req.id)
            return user_post_convert_response(item)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
            return user_post_convert_response(None)

    def BatchUpdateUserPost(self, req:user_post_pb2.BatchUpdateUserPostRequest, context):
        """批量修改状态
        """
        from recruit_srv.config.config import DB
        with DB.atomic() as transaction:
            try:
                model = UserPost.update(status=req.status,remark=req.remark,review_id=req.review_id)\
                    .where(UserPost.id << list(req.ids))
                model.execute()
            except Exception as e:
                transaction.rollback()
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(f"内部错误  {e}")
            finally:
                return google.protobuf.empty_pb2.Empty()
