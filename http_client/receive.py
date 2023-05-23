import os
import time

def receive_multiple(client_id: int, topic: str, benchmark_file: str, no: int=1):
    for _ in range(no):
        receive(client_id, topic, benchmark_file)

def receive(client_id: int, topic: str, benchmark_file: str,):
    start = time.time()
    os.system(f'curl -s localhost:5000/subscription/{topic}/{client_id} -X GET >> /dev/null')
    end = time.time()
    delta = end - start
    os.system(f'echo {delta} >> data/benchmarks/receive/{benchmark_file}')
