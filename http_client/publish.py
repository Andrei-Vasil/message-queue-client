import json
import os
import time
import requests

def publish_multiple(topic: str, request_file: str, benchmark_file: str, no: int=1):
    for i in range(no):
        publish(topic, request_file, benchmark_file, i)

def publish(topic: str, request_file: str, benchmark_file: str, id: int):
    with open(request_file, 'r+') as f:
        data = json.load(f)
        data['benchmark_id'] = id
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    start = time.time()
    with open(request_file, "rb") as f:
        requests.post(f'http://localhost:5000/publish/{topic}', headers={'Content-Type': 'application/json'}, data=f)
    os.system(f'echo {start},{id} >> data/benchmarks/publish/{benchmark_file}')
