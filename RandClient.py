from __future__ import print_function

import grpc

import Rand_pb2
import Rand_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = Rand_pb2_grpc.RandValuesStub(channel)
    response = stub.RandValue(Rand_pb2.RandRequest(SendText=True, SendNumber=True))
    print("Random Number: " + str(response.Number))
    print("Random Text: " + response.Text)


if __name__ == '__main__':
    run()