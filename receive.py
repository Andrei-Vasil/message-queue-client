import os
import time

from benchmark_constants import BENCHMARK_FILE

def receive_multiple(client_id: int, topic: str, no: int=1):
    for _ in range(no):
        receive(client_id, topic)

def receive(client_id: int, topic: str):
    start = time.time()
    os.system(f'curl -s localhost:5000/subscription/{topic}/{client_id} -X GET >> /dev/null')
    end = time.time()
    delta = end - start
    os.system(f'echo {delta} >> data/benchmarks/receive/{BENCHMARK_FILE}')
