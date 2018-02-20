from concurrent import futures
import time
import random
import string

import grpc

import Rand_pb2
import Rand_pb2_grpc

import scratch

class RandValues(Rand_pb2_grpc.RandValuesServicer):
    def RandValue(self, request, context):
        returnText = ""
        returnNumber = None

        if request.SendText:
            if request.TextLength:
                for i in range(0, request.TextLength):
                    returnText += random.choice(string.ascii_letters)
        
        if request.SendNumber:
            if request.NumberFloor < request.NumberCeiling:
                returnNumber = random.randint(request.NumberFloor, request.NumberCeiling)
            else: returnNumber = random.randint(0, 1000000)

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
    scratch.scratchFunc()
    # serve()