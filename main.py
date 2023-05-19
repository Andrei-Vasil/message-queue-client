import os
import time
request_file = 'requests/1mb.json'

import json

id = 1

with open(request_file, 'r+') as f:
    data = json.load(f)
    data['id'] = id
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()

os.system('curl localhost:5000/topic/topic1 -X POST')
os.system('curl localhost:5000/subscription/topic1 -X POST')

start = time.time()
os.system(f'curl localhost:5000/publish/topic1 -H "Content-Type: application/json" -X POST -d @{request_file}')
end = time.time()
delta = end - start
print(f'delta publish: {delta}')


start = time.time()
os.system(f'curl localhost:5000/subscription/topic1/0 -X GET >> /dev/null')
end = time.time()
delta = end - start
print(f'delta receive: {delta}')

