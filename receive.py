import os
import time

benchmark_coding_languages = ["rust", "cpp", "python-async", "python-multithreaded"]
benchmark_coding_language = "cpp"
benchmark_id = 2
benchmark_file = f'2023-05-19-{benchmark_id}-{benchmark_coding_language}.csv'

def receive_multiple(client_id: int, topic: str, no: int=1):
    for _ in range(no):
        receive(client_id, topic)

def receive(client_id: int, topic: str):
    start = time.time()
    os.system(f'curl -s localhost:5000/subscription/{topic}/{client_id} -X GET >> /dev/null')
    end = time.time()
    delta = end - start
    os.system(f'echo {delta} >> data/benchmarks/receive/{benchmark_file}')
