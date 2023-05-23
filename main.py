import json
from methodologies import Methodologies
from benchmark_constants import CODING_LANGUAGE, REQUEST_FILES

TOPIC = 'topic1'

def main():
    with open('scenarios.json') as f:
        scenarios = dict(json.load(f))
        for scenario_key, scenario in scenarios.items():
            if scenario_key != 'throughput':
                benchmark_latency(scenario)
            else:
                benchmark_throughput(scenario)

def benchmark_latency(scenarios: list[dict]):
    for scenario in scenarios:
        file_path = scenario['file_path']
        no_of_requests = scenario['no_of_requests']
        total_size = scenario['total_size']

def benchmark_throughput(scenarios: list[dict]):
    pass

def call_all_methodologies(file_path: str, no_of_requests: int, total_size: str):
    Methodologies.one2one(file_path, no_of_requests, total_size)
    Methodologies.one2many(file_path, no_of_requests, total_size)
    Methodologies.many2one(file_path, no_of_requests, total_size)
    Methodologies.many2many(file_path, no_of_requests, total_size)

if __name__ == "__main__":
    main()
