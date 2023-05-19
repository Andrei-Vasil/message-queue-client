import json
import os
import time

def publish_multiple(topic: str, request_file: str, no: int=1):
    for i in range(no):
        publish(topic, request_file, i)

def publish(topic: str, request_file: str, id: int):
    with open(request_file, 'r+') as f:
        data = json.load(f)
        data['id'] = id
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    start = time.time()
    os.system(f'curl localhost:5000/publish/{topic} -H "Content-Type: application/json" -X POST -d @{request_file}')
    end = time.time()
    delta = end - start
    # print(f'delta publish: {delta}')

