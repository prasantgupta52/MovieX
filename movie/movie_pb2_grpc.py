# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import movie_pb2 as movie__pb2


class MovieServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAll = channel.unary_unary(
                '/moviePackage.MovieService/GetAll',
                request_serializer=movie__pb2.Empty.SerializeToString,
                response_deserializer=movie__pb2.MovieCardResponse.FromString,
                )
        self.GetPlaying = channel.unary_unary(
                '/moviePackage.MovieService/GetPlaying',
                request_serializer=movie__pb2.Empty.SerializeToString,
                response_deserializer=movie__pb2.MovieCardResponse.FromString,
                )
        self.GetComing = channel.unary_unary(
                '/moviePackage.MovieService/GetComing',
                request_serializer=movie__pb2.Empty.SerializeToString,
                response_deserializer=movie__pb2.MovieCardResponse.FromString,
                )
        self.GetAMovie = channel.unary_unary(
                '/moviePackage.MovieService/GetAMovie',
                request_serializer=movie__pb2.MovieRequest.SerializeToString,
                response_deserializer=movie__pb2.MovieBgResponse.FromString,
                )
        self.UpdateReservedMovieInfo = channel.unary_unary(
                '/moviePackage.MovieService/UpdateReservedMovieInfo',
                request_serializer=movie__pb2.UpdateMovieInfoRequest.SerializeToString,
                response_deserializer=movie__pb2.UpdateMovieInfoResponse.FromString,
                )


class MovieServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlaying(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetComing(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAMovie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateReservedMovieInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MovieServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=movie__pb2.Empty.FromString,
                    response_serializer=movie__pb2.MovieCardResponse.SerializeToString,
            ),
            'GetPlaying': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlaying,
                    request_deserializer=movie__pb2.Empty.FromString,
                    response_serializer=movie__pb2.MovieCardResponse.SerializeToString,
            ),
            'GetComing': grpc.unary_unary_rpc_method_handler(
                    servicer.GetComing,
                    request_deserializer=movie__pb2.Empty.FromString,
                    response_serializer=movie__pb2.MovieCardResponse.SerializeToString,
            ),
            'GetAMovie': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAMovie,
                    request_deserializer=movie__pb2.MovieRequest.FromString,
                    response_serializer=movie__pb2.MovieBgResponse.SerializeToString,
            ),
            'UpdateReservedMovieInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateReservedMovieInfo,
                    request_deserializer=movie__pb2.UpdateMovieInfoRequest.FromString,
                    response_serializer=movie__pb2.UpdateMovieInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'moviePackage.MovieService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MovieService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/moviePackage.MovieService/GetAll',
            movie__pb2.Empty.SerializeToString,
            movie__pb2.MovieCardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlaying(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/moviePackage.MovieService/GetPlaying',
            movie__pb2.Empty.SerializeToString,
            movie__pb2.MovieCardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetComing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/moviePackage.MovieService/GetComing',
            movie__pb2.Empty.SerializeToString,
            movie__pb2.MovieCardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAMovie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/moviePackage.MovieService/GetAMovie',
            movie__pb2.MovieRequest.SerializeToString,
            movie__pb2.MovieBgResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateReservedMovieInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/moviePackage.MovieService/UpdateReservedMovieInfo',
            movie__pb2.UpdateMovieInfoRequest.SerializeToString,
            movie__pb2.UpdateMovieInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)