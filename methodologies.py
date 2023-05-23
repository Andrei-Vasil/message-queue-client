from http_client.misc import create_topic, subscribe, unsubscribe, delete_topic

TOPIC = 'topic1'


class Methodologies:
    @staticmethod
    def one2one(file_path: str, no_of_requests: int, total_size: str):
        BENCHMARK_FILE = f'{datetime.date.today()}-{BENCHMARK_ID}-{BENCHMARK_CODING_LANGUAGE}.csv'
        create_topic(TOPIC)
        id = subscribe(TOPIC)

        unsubscribe(TOPIC, id)
        delete_topic(TOPIC)

    @staticmethod
    def one2many(file_path: str, no_of_requests: int, total_size: str):
        pass

    @staticmethod
    def many2one(file_path: str, no_of_requests: int, total_size: str):
        pass

    @staticmethod
    def many2many(file_path: str, no_of_requests: int, total_size: str):
        pass
