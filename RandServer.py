from concurrent import futures
import time
import random

import grpc

import Rand_pb2
import Rand_pb2_grpc

class RandValues(Rand_pb2_grpc.RandValuesServicer):
    returnText = None
    returnNumber = None

    def RandValue(self, request, context):
        if request.SendText:
            returnText = "random text"
        
        if request.SendNumber:
            returnNumber = 999

        return Rand_pb2.RandResponse(Text=returnText, Number=returnNumber)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Rand_pb2_grpc.add_RandValuesServicer_to_server(RandValues(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()