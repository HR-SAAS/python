# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import counter_pb2 as counter__pb2


class MessageCounterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CountUserMessage = channel.unary_unary(
                '/MessageCounter/CountUserMessage',
                request_serializer=counter__pb2.CountUserMessageRequest.SerializeToString,
                response_deserializer=counter__pb2.CountUserMessageResponse.FromString,
                )


class MessageCounterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CountUserMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageCounterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CountUserMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.CountUserMessage,
                    request_deserializer=counter__pb2.CountUserMessageRequest.FromString,
                    response_serializer=counter__pb2.CountUserMessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MessageCounter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MessageCounter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CountUserMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageCounter/CountUserMessage',
            counter__pb2.CountUserMessageRequest.SerializeToString,
            counter__pb2.CountUserMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
