import json
from methodologies import Methodologies

def main():
    with open('scenarios.json') as f:
        scenarios = dict(json.load(f))
        for scenario_key, scenario in scenarios.items():
            if scenario_key != 'latency_by_message_size':
                continue
            if scenario_key != 'throughput':
                benchmark_latency(scenario)
            else:
                benchmark_throughput(scenario)

def benchmark_latency(scenarios: list[dict]):
    for scenario in scenarios:
        id = scenario['id']
        file_path = scenario['file_path']
        no_of_requests = int(scenario['no_of_requests'])
        total_size = scenario['total_size']
        call_all_methodologies(id, file_path, no_of_requests, total_size)

def benchmark_throughput(scenarios: list[dict]):
    for scenario in scenarios:
        file_path = scenario['file_path']
        spin_offs = list(scenario['spin_offs'])
        for spin_off in spin_offs:
            id = spin_off['id']
            no_of_requests = int(spin_off['no_of_requests'])
            total_size = spin_off['total_size']
            call_all_methodologies(id, file_path, no_of_requests, total_size)


def call_all_methodologies(id: str, file_path: str, no_of_requests: int, total_size: str):
    Methodologies.one2one(f'one2one_{id}', file_path, no_of_requests, total_size)
    Methodologies.one2many(f'one2many_{id}', file_path, no_of_requests, total_size)
    Methodologies.many2one(f'many2one_{id}', file_path, no_of_requests, total_size)
    Methodologies.many2many(f'many2many_{id}', file_path, no_of_requests, total_size)

if __name__ == "__main__":
    main()
