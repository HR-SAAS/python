# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import department_pb2 as department__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DepartmentStub(object):
    """部门
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDepartmentList = channel.unary_unary(
                '/Department/GetDepartmentList',
                request_serializer=department__pb2.GetDepartmentListRequest.SerializeToString,
                response_deserializer=department__pb2.DepartmentListResponse.FromString,
                )
        self.GetDepartmentDetail = channel.unary_unary(
                '/Department/GetDepartmentDetail',
                request_serializer=department__pb2.GetDepartmentDetailRequest.SerializeToString,
                response_deserializer=department__pb2.DepartmentResponse.FromString,
                )
        self.CreateDepartment = channel.unary_unary(
                '/Department/CreateDepartment',
                request_serializer=department__pb2.CreateDepartmentRequest.SerializeToString,
                response_deserializer=department__pb2.DepartmentResponse.FromString,
                )
        self.UpdateDepartment = channel.unary_unary(
                '/Department/UpdateDepartment',
                request_serializer=department__pb2.UpdateDepartmentRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteDepartment = channel.unary_unary(
                '/Department/DeleteDepartment',
                request_serializer=department__pb2.DeleteDepartmentRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class DepartmentServicer(object):
    """部门
    """

    def GetDepartmentList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDepartmentDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDepartment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDepartment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDepartment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DepartmentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDepartmentList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDepartmentList,
                    request_deserializer=department__pb2.GetDepartmentListRequest.FromString,
                    response_serializer=department__pb2.DepartmentListResponse.SerializeToString,
            ),
            'GetDepartmentDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDepartmentDetail,
                    request_deserializer=department__pb2.GetDepartmentDetailRequest.FromString,
                    response_serializer=department__pb2.DepartmentResponse.SerializeToString,
            ),
            'CreateDepartment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDepartment,
                    request_deserializer=department__pb2.CreateDepartmentRequest.FromString,
                    response_serializer=department__pb2.DepartmentResponse.SerializeToString,
            ),
            'UpdateDepartment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDepartment,
                    request_deserializer=department__pb2.UpdateDepartmentRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteDepartment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDepartment,
                    request_deserializer=department__pb2.DeleteDepartmentRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Department', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Department(object):
    """部门
    """

    @staticmethod
    def GetDepartmentList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Department/GetDepartmentList',
            department__pb2.GetDepartmentListRequest.SerializeToString,
            department__pb2.DepartmentListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDepartmentDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Department/GetDepartmentDetail',
            department__pb2.GetDepartmentDetailRequest.SerializeToString,
            department__pb2.DepartmentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDepartment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Department/CreateDepartment',
            department__pb2.CreateDepartmentRequest.SerializeToString,
            department__pb2.DepartmentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDepartment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Department/UpdateDepartment',
            department__pb2.UpdateDepartmentRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDepartment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Department/DeleteDepartment',
            department__pb2.DeleteDepartmentRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
