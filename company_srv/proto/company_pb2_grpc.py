# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import common_pb2 as common__pb2
from . import company_pb2 as company__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CompanyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCompanyList = channel.unary_unary(
                '/Company/GetCompanyList',
                request_serializer=company__pb2.GetCompanyListRequest.SerializeToString,
                response_deserializer=company__pb2.CompanyListResponse.FromString,
                )
        self.GetCompanyDetail = channel.unary_unary(
                '/Company/GetCompanyDetail',
                request_serializer=company__pb2.GetCompanyDetailRequest.SerializeToString,
                response_deserializer=company__pb2.CompanyResponse.FromString,
                )
        self.CreateCompany = channel.unary_unary(
                '/Company/CreateCompany',
                request_serializer=company__pb2.CreateCompanyRequest.SerializeToString,
                response_deserializer=company__pb2.CompanyResponse.FromString,
                )
        self.UpdateCompany = channel.unary_unary(
                '/Company/UpdateCompany',
                request_serializer=company__pb2.UpdateCompanyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteCompany = channel.unary_unary(
                '/Company/DeleteCompany',
                request_serializer=company__pb2.DeleteCompanyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetMyCompanyList = channel.unary_unary(
                '/Company/GetMyCompanyList',
                request_serializer=company__pb2.GetMyCompanyListRequest.SerializeToString,
                response_deserializer=company__pb2.CompanyListResponse.FromString,
                )
        self.GetCompanyUserIdList = channel.unary_unary(
                '/Company/GetCompanyUserIdList',
                request_serializer=company__pb2.GetCompanyUserListRequest.SerializeToString,
                response_deserializer=common__pb2.UserIdList.FromString,
                )
        self.CreateUserCompany = channel.unary_unary(
                '/Company/CreateUserCompany',
                request_serializer=company__pb2.SaveUserCompanyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateUserCompany = channel.unary_unary(
                '/Company/UpdateUserCompany',
                request_serializer=company__pb2.SaveUserCompanyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteUserCompany = channel.unary_unary(
                '/Company/DeleteUserCompany',
                request_serializer=company__pb2.DeleteUserCompanyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class CompanyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCompanyList(self, request, context):
        """获取公司列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCompanyDetail(self, request, context):
        """获取公司详情
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCompany(self, request, context):
        """创建公司
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCompany(self, request, context):
        """更新公司信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCompany(self, request, context):
        """删除公司
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMyCompanyList(self, request, context):
        """获取我都公司列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCompanyUserIdList(self, request, context):
        """公司下所有用户,分页
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUserCompany(self, request, context):
        """加入公司
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserCompany(self, request, context):
        """关系更新
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUserCompany(self, request, context):
        """删除用户公司
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CompanyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCompanyList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCompanyList,
                    request_deserializer=company__pb2.GetCompanyListRequest.FromString,
                    response_serializer=company__pb2.CompanyListResponse.SerializeToString,
            ),
            'GetCompanyDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCompanyDetail,
                    request_deserializer=company__pb2.GetCompanyDetailRequest.FromString,
                    response_serializer=company__pb2.CompanyResponse.SerializeToString,
            ),
            'CreateCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCompany,
                    request_deserializer=company__pb2.CreateCompanyRequest.FromString,
                    response_serializer=company__pb2.CompanyResponse.SerializeToString,
            ),
            'UpdateCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCompany,
                    request_deserializer=company__pb2.UpdateCompanyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCompany,
                    request_deserializer=company__pb2.DeleteCompanyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetMyCompanyList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMyCompanyList,
                    request_deserializer=company__pb2.GetMyCompanyListRequest.FromString,
                    response_serializer=company__pb2.CompanyListResponse.SerializeToString,
            ),
            'GetCompanyUserIdList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCompanyUserIdList,
                    request_deserializer=company__pb2.GetCompanyUserListRequest.FromString,
                    response_serializer=common__pb2.UserIdList.SerializeToString,
            ),
            'CreateUserCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUserCompany,
                    request_deserializer=company__pb2.SaveUserCompanyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateUserCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserCompany,
                    request_deserializer=company__pb2.SaveUserCompanyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteUserCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUserCompany,
                    request_deserializer=company__pb2.DeleteUserCompanyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Company', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Company(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCompanyList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/GetCompanyList',
            company__pb2.GetCompanyListRequest.SerializeToString,
            company__pb2.CompanyListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCompanyDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/GetCompanyDetail',
            company__pb2.GetCompanyDetailRequest.SerializeToString,
            company__pb2.CompanyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/CreateCompany',
            company__pb2.CreateCompanyRequest.SerializeToString,
            company__pb2.CompanyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/UpdateCompany',
            company__pb2.UpdateCompanyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/DeleteCompany',
            company__pb2.DeleteCompanyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMyCompanyList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/GetMyCompanyList',
            company__pb2.GetMyCompanyListRequest.SerializeToString,
            company__pb2.CompanyListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCompanyUserIdList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/GetCompanyUserIdList',
            company__pb2.GetCompanyUserListRequest.SerializeToString,
            common__pb2.UserIdList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUserCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/CreateUserCompany',
            company__pb2.SaveUserCompanyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUserCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/UpdateUserCompany',
            company__pb2.SaveUserCompanyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUserCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Company/DeleteUserCompany',
            company__pb2.DeleteUserCompanyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
