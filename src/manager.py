#!/usr/bin/env python3
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

port = 50002
address = ('localhost', port)
key = b"azerty"


class QueueClient:
    def __init__(self):
        # get the queues from the manager
        QueueManager.register("get_task_queue")
        QueueManager.register("get_result_queue")
        # connect the client on the same address and port as the manager
        # with the key
        self.client = QueueManager(address, key)
        self.client.connect()
        # get a ref to the manager queues
        self.task_queue_ref = self.client.get_task_queue()
        self.result_queue_ref = self.client.get_result_queue()


class QueueManager(BaseManager):
    def __init__(self, address, key):
        """
        Contient les Queues des taches et des resultats
        """
        # call the parent class constructor
        super().__init__(address=address, authkey=key)
        self.task_queue = Queue()
        self.result_queue = Queue()

        # create the methodes to get the queue
        self.register("get_task_queue", callable=lambda:self.task_queue)
        self.register("get_result_queue", callable=lambda:self.result_queue)
        
    def run(self):
        # get the server object
        self.server = self.get_server()
        # make the server run until we kill it
        self.server.serve_forever()


if __name__ == "__main__":
    # create a single QueueManager instance
    my_queue_manager = QueueManager(address, key)
    my_queue_manager.run()
