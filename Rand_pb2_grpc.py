# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Rand_pb2 as Rand__pb2


class RandValuesStub(object):
  """service def
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RandValue = channel.unary_unary(
        '/pkg_Rand.RandValues/RandValue',
        request_serializer=Rand__pb2.RandRequest.SerializeToString,
        response_deserializer=Rand__pb2.RandResponse.FromString,
        )


class RandValuesServicer(object):
  """service def
  """

  def RandValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RandValuesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RandValue': grpc.unary_unary_rpc_method_handler(
          servicer.RandValue,
          request_deserializer=Rand__pb2.RandRequest.FromString,
          response_serializer=Rand__pb2.RandResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pkg_Rand.RandValues', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
