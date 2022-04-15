import google.protobuf.empty_pb2
import grpc

from resume_srv.proto import resume_pb2,resume_pb2_grpc
from resume_srv.model.model import Resume

from loguru import logger
from peewee import DoesNotExist


def resume_convert_response(company):
    item = resume_pb2.ResumeResponse()
    item.id = company.id
    return convert_resume(company, item)


def response_convert_resume(request):
    item = Resume()
    return convert_resume(request, item)


def convert_resume(source, to):
    for i in [
        "user_id",
        "name",
        "type",
        "tag",
        "content",
        "post_count",
        "status",
    ]:
        temp = getattr(source, i)
        if temp is not None and temp != -1 and temp != "":
            setattr(to, i, temp)
    return to


class ResumeService(resume_pb2_grpc.ResumeServicer):

    @logger.catch
    def GetResumeList(self, req: resume_pb2.GetResumeListRequest, context):
        """获取简历列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    @logger.catch
    def CreateResume(self, req:resume_pb2.CreateResumeRequest, context):
        """创建简历
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    @logger.catch
    def UpdateResume(self, req:resume_pb2.UpdateResumeRequest, context):
        """更新简历
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    @logger.catch
    def DeleteResume(self, req:resume_pb2.DeleteResumeRequest, context):
        """删除简历
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
