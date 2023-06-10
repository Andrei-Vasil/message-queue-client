import os
import time
from benchmark_constants import CODING_LANGUAGE, MANY, ONE, TOPIC
from http_client.misc import create_topic, subscribe, unsubscribe, delete_topic
from http_client.publish import publish_multiple
from http_client.receive import receive_multiple

# TODO: for each benchmark up to many2many_throughput_1b_5mil (cpp) & each benchmark from python-async:
#       consumer time is (time.time() - t1) instead of (time.time() - t2) 
#       => actual consumer total time = consumer total time - producer total time
# T1 -> F1~T2 -> F2
# a = F1~T2 - T1 # producer time
# b = F2 - T1 # wrongly calculated consumer time
# c = b - a = F2 - T2 # actual consumer time
class Methodologies:
    @staticmethod
    def __general(id: str, file_path: str, no_of_requests: int, total_size: str, no_of_producers: int, no_of_clients: int):
        benchmark_file = f'{id}-{CODING_LANGUAGE}.csv'

        create_topic(TOPIC)
        client_ids = [subscribe(TOPIC) for _ in range(no_of_clients)]

        prod_pid = os.fork()
        if prod_pid == 0:
            t1 = time.time()
            prod_pids = []
            for producer_idx in range(no_of_producers):
                pid = os.fork()
                if pid == 0:
                    publish_multiple(TOPIC, f'data/requests/{producer_idx}/{file_path}', benchmark_file, id, no=no_of_requests // no_of_producers, start=producer_idx * (no_of_requests // no_of_producers))
                    exit(0)
                prod_pids.append(pid)
            for pid in prod_pids:
                os.waitpid(pid, 0)
            os.system(f'echo "Producer {id}-{CODING_LANGUAGE} {no_of_producers}to{no_of_clients} Total size: {total_size} Total time: {time.time() - t1}" >> data/benchmarks/total_time.txt')
            print('finish write', time.time() - t1)
            exit(0)

        os.waitpid(prod_pid, 0)

        recv_pid = os.fork()
        if recv_pid == 0:
            t2 = time.time()
            recv_pids = []
            for client_id in client_ids:
                pid = os.fork()
                if pid == 0:
                    receive_multiple(client_id, TOPIC, benchmark_file, id, no=no_of_requests)
                    exit(0)
                recv_pids.append(pid)
            for pid in recv_pids:
                os.waitpid(pid, 0)
            os.system(f'echo "Consumer {id}-{CODING_LANGUAGE} {no_of_producers}to{no_of_clients} Total size: {total_size} Total time: {time.time() - t2}" >> data/benchmarks/total_time.txt')
            print('finish read', time.time() - t2)
            exit(0)

        os.waitpid(recv_pid, 0)

        for client_id in client_ids:
            unsubscribe(TOPIC, client_id)
        delete_topic(TOPIC)
        print(f'benchmark {id} {no_of_producers}to{no_of_clients} ended')

    @staticmethod
    def one2one(id: str, file_path: str, no_of_requests: int, total_size: str):
        Methodologies.__general(id, file_path, no_of_requests, total_size, ONE, ONE)

    @staticmethod
    def one2many(id: str, file_path: str, no_of_requests: int, total_size: str):
        Methodologies.__general(id, file_path, no_of_requests, total_size, ONE, MANY)

    @staticmethod
    def many2one(id: str, file_path: str, no_of_requests: int, total_size: str):
        Methodologies.__general(id, file_path, no_of_requests, total_size, MANY, ONE)

    @staticmethod
    def many2many(id: str, file_path: str, no_of_requests: int, total_size: str):
        Methodologies.__general(id, file_path, no_of_requests, total_size, MANY, MANY)
