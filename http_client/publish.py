import json
import os
import time
import requests

def publish_multiple(topic: str, request_file: str, benchmark_file: str, scenario_id: str, no: int=1, start: int=0):
    for i in range(start, start + no):
        publish(topic, request_file, benchmark_file, scenario_id, i)

def publish(topic: str, request_file: str, benchmark_file: str, scenario_id: str, id: int):
    with open(request_file, 'r+') as f:
        data = json.load(f)
        data['benchmark_id'] = id
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    start = time.time()
    try:
        with open(request_file, "r") as f:
            body = json.load(f)
            requests.post(f'http://localhost:5000/publish/{topic}/{scenario_id}', headers={'Content-Type': 'application/json'}, json=body)
    except Exception as e:
        os.system(f'curl -s localhost:5000/publish/{topic}/{scenario_id} -H "Content-Type: application/json" -X POST -d @{request_file} >> /dev/null')
    os.system(f'echo {start},{id} >> data/benchmarks/publish/{benchmark_file}')
