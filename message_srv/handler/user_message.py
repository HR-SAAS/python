import json

import google.protobuf.empty_pb2
import grpc

from common.utils import build_model_filters
from message_srv.proto import user_message_pb2, user_message_pb2_grpc
from message_srv.model.model import UserMessage

from loguru import logger
from peewee import DoesNotExist, Value, SQL


def resume_convert_response(user_message):
    item = user_message_pb2.MessageResponse()
    item.id = user_message.id
    item.created_at.FromDatetime(user_message.created_at)
    item.updated_at.FromDatetime(user_message.updated_at)
    return convert_resume(user_message, item)


def response_convert_user_message(request):
    item = UserMessage()
    return convert_resume(request, item)


def convert_resume(source, to):
    for i in [
        "user_id",
        "source_type",
        "source_id",
        "type",
        "content",
        "is_read",
        "status",
        "relation_id",
        "relation_type"
    ]:
        temp = getattr(source, i)
        if temp is not None and temp != -1 and temp != "":
            setattr(to, i, temp)
    return to


class UserMessageService(user_message_pb2_grpc.UserMessageServicer):

    @logger.catch
    def GetMessageList(self, req: user_message_pb2.GetMessageListRequest, context):
        """获取简历列表
        """
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        stat = limit * (page - 1)

        model = UserMessage.select()

        if req.search is not None:
            search = req.search
            if search['user_id']:
                model = model.where(UserMessage.user_id == search['user_id'])

        if req.sort is not None:
            for i, v in dict(req.sort).items():
                model = model.order_by(i, v)
        # 动态search
        rsp = user_message_pb2.MessageListResponse()

        rsp.total = model.count()
        data = model.limit(limit).offset(stat)
        print(data)
        for item in data:
            rsp.data.append(resume_convert_response(item))
        return rsp

    @logger.catch
    def CreateMessage(self, req: user_message_pb2.CreateMessageRequest, context):
        """创建简历
        """
        resume = response_convert_user_message(req)
        resume.save()
        return resume_convert_response(resume)

    @logger.catch
    def UpdateMessage(self, req: user_message_pb2.UpdateMessageRequest, context):
        """更新简历
        """
        from message_srv.config.config import DB
        with DB.atomic() as transaction:
            try:

                item = response_convert_user_message(req)
                item.save()
                # 同时创建关联
                return resume_convert_response(item)
            except Exception as e:
                transaction.rollback()
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(f"内部错误  {e}")
                return user_message_pb2.MessageResponse()

    @logger.catch
    def DeleteMessage(self, req: user_message_pb2.DeleteMessageRequest, context):
        """删除简历
        """
        try:
            item = UserMessage.get_by_id(req.id)
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
    def GetMessageDetail(self, req: user_message_pb2.GetMessageDetailRequest, context):
        """详情
        """
        item = UserMessage.get_by_id(req.id)
        return resume_convert_response(item)
