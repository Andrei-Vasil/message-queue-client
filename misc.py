import os
import random
import string


def create_topic(topic: str):
    os.system(f'curl -s localhost:5000/topic/{topic} -X POST > /dev/null')

def subscribe(topic: str) -> int:
    random_token = ''.join(random.choice([*string.digits, *string.ascii_letters]) for _ in range(10))
    os.system(f'curl -s localhost:5000/subscription/{topic} -X POST > data/subscription_{random_token}.txt')
    with open(f'data/subscription_{random_token}.txt', 'r+') as f:
        id = int(f.readline())
    os.system(f'rm data/subscription_{random_token}.txt')
    return id
