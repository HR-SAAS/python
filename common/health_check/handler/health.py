import grpc

from common.health_check.proto import health_pb2,health_pb2_grpc


class HealthService(health_pb2_grpc.HealthServicer):
    def Check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        return health_pb2.HealthCheckResponse(status=1)

    def Watch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        return health_pb2.HealthCheckResponse(status=1)
