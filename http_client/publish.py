import json
import os
import time
import requests

def publish_multiple(topic: str, request_file: str, benchmark_file: str, scenario_id: str, no: int=1):
    for i in range(no):
        publish(topic, request_file, benchmark_file, scenario_id, i)

def publish(topic: str, request_file: str, benchmark_file: str, scenario_id: str, id: int):
    with open(request_file, 'r+') as f:
        data = json.load(f)
        data['benchmark_id'] = id
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    start = time.time()
    with open(request_file, "rb") as f:
        requests.post(f'http://localhost:5000/publish/{topic}/{scenario_id}', headers={'Content-Type': 'application/json'}, data=f)
    os.system(f'echo {start},{id} >> data/benchmarks/publish/{benchmark_file}')
