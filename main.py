from multiprocessing import Process
from receive import receive_multiple
from publish import publish_multiple
from misc import create_topic, subscribe

request_file = 'data/requests/1mb.json'
topic = 'topic1'

def main():
    create_topic(topic)
    id = subscribe(topic)
    no_of_iterations = 500
    publish_multiple(topic, request_file, no_of_iterations)
    print('publish done')
    receive_multiple(id, topic, no_of_iterations)
    print('receive done')

    # publish_process = Process(target=publish_multiple, args=(topic, request_file, 100,))
    # publish_process.start()

    # receive_process = Process(target=receive_multiple, args=(id, topic, 100,))
    # receive_process.start()

    # publish_process.join()
    # receive_process.join()


if __name__ == "__main__":
    main()
