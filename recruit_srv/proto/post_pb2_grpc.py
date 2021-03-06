# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import post_pb2 as post__pb2


class PostStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPostList = channel.unary_unary(
                '/Post/GetPostList',
                request_serializer=post__pb2.GetPostListRequest.SerializeToString,
                response_deserializer=post__pb2.PostListResponse.FromString,
                )
        self.CreatePost = channel.unary_unary(
                '/Post/CreatePost',
                request_serializer=post__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=post__pb2.PostResponse.FromString,
                )
        self.UpdatePost = channel.unary_unary(
                '/Post/UpdatePost',
                request_serializer=post__pb2.UpdatePostRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeletePost = channel.unary_unary(
                '/Post/DeletePost',
                request_serializer=post__pb2.DeletePostRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetPostDetail = channel.unary_unary(
                '/Post/GetPostDetail',
                request_serializer=post__pb2.GetPostDetailRequest.SerializeToString,
                response_deserializer=post__pb2.PostResponse.FromString,
                )
        self.GetPostListByIds = channel.unary_unary(
                '/Post/GetPostListByIds',
                request_serializer=post__pb2.GetPostListByIdsRequest.SerializeToString,
                response_deserializer=post__pb2.PostListResponse.FromString,
                )


class PostServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPostList(self, request, context):
        """??????????????????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePost(self, request, context):
        """????????????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePost(self, request, context):
        """????????????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePost(self, request, context):
        """????????????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPostDetail(self, request, context):
        """??????????????????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPostListByIds(self, request, context):
        """??????id????????????
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPostList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPostList,
                    request_deserializer=post__pb2.GetPostListRequest.FromString,
                    response_serializer=post__pb2.PostListResponse.SerializeToString,
            ),
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=post__pb2.CreatePostRequest.FromString,
                    response_serializer=post__pb2.PostResponse.SerializeToString,
            ),
            'UpdatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePost,
                    request_deserializer=post__pb2.UpdatePostRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeletePost': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePost,
                    request_deserializer=post__pb2.DeletePostRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetPostDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPostDetail,
                    request_deserializer=post__pb2.GetPostDetailRequest.FromString,
                    response_serializer=post__pb2.PostResponse.SerializeToString,
            ),
            'GetPostListByIds': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPostListByIds,
                    request_deserializer=post__pb2.GetPostListByIdsRequest.FromString,
                    response_serializer=post__pb2.PostListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Post', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Post(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPostList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Post/GetPostList',
            post__pb2.GetPostListRequest.SerializeToString,
            post__pb2.PostListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Post/CreatePost',
            post__pb2.CreatePostRequest.SerializeToString,
            post__pb2.PostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Post/UpdatePost',
            post__pb2.UpdatePostRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Post/DeletePost',
            post__pb2.DeletePostRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPostDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Post/GetPostDetail',
            post__pb2.GetPostDetailRequest.SerializeToString,
            post__pb2.PostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPostListByIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Post/GetPostListByIds',
            post__pb2.GetPostListByIdsRequest.SerializeToString,
            post__pb2.PostListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
