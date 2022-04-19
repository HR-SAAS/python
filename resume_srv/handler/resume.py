import json

import google.protobuf.empty_pb2
import grpc

from common.utils import build_model_filters
from resume_srv.proto import resume_pb2, resume_pb2_grpc
from resume_srv.model.model import Resume

from loguru import logger
from peewee import DoesNotExist, Value, SQL


def resume_convert_response(resume):
    item = resume_pb2.ResumeResponse()
    if resume is None:
        return item
    item.id = resume.id
    item.post_count = resume.post_count
    item.created_at.FromDatetime(resume.created_at)
    item.created_at.FromDatetime(resume.updated_at)
    return convert_resume(resume, item)


def response_convert_resume(request):
    item = Resume()
    return convert_resume(request, item)


def convert_resume(source, to):
    for i in [
        "name",
        "type",
        "content",
        "status",
        "user_id",
    ]:
        temp = getattr(source, i)
        if temp is not None and temp != -1 and temp != "":
            setattr(to, i, temp)
    if isinstance(source, Resume):
        for i in source.tag:
            to.tag.append(i)
    else:
        to.tag = source.tag
    return to


class ResumeService(resume_pb2_grpc.ResumeServicer):

    @logger.catch
    def GetResumeList(self, req: resume_pb2.GetResumeListRequest, context):
        """获取简历列表
        """
        page = 1
        limit = 15
        if req.page:
            page = req.page
        if req.limit:
            limit = req.limit
        stat = limit * (page - 1)

        model = Resume.select()

        if req.search is not None:
            search = req.search
            if search['user_id']:
                model = model.where(Resume.user_id == search['user_id'])

        if req.sort is not None:
            for i,v in dict(req.sort).items():
                model = model.order_by(i,v)
        # 动态search
        rsp = resume_pb2.ResumeListResponse()

        rsp.total = model.count()
        data = model.limit(limit).offset(stat)
        print(data)
        for item in data:
            rsp.data.append(resume_convert_response(item))
        return rsp

    @logger.catch
    def CreateResume(self, req: resume_pb2.CreateResumeRequest, context):
        """创建简历
        """
        logger.info(req.tag)
        resume = response_convert_resume(req)
        resume.save()
        return resume_convert_response(resume)

    @logger.catch
    def UpdateResume(self, req: resume_pb2.UpdateResumeRequest, context):
        """更新简历
        """
        from resume_srv.config.config import DB
        with DB.atomic() as transaction:
            try:

                item = response_convert_resume(req)
                item.save()
                # 同时创建关联
                return resume_convert_response(item)
            except Exception as e:
                transaction.rollback()
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(f"内部错误  {e}")
                return resume_pb2.ResumeResponse()

    @logger.catch
    def DeleteResume(self, req: resume_pb2.DeleteResumeRequest, context):
        """删除简历
        """
        try:
            item = Resume.get_by_id(req.id)
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
    def GetResumeDetail(self, req: resume_pb2.GetResumeDetailRequest, context):
        """详情
        """
        try:
            item = Resume.get_by_id(req.id)
            return resume_convert_response(item)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("找不到数据")
            return resume_convert_response(None)

