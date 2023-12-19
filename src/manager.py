#!/usr/bin/env python3
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

port = 50000
key = b"azerty"


class QueueClient:
    def __init__(self):
        self.task_queue_ref
        self.task_queue_ref


class QueueManager(BaseManager):
    def __init__(self):
        """
        Contient les Queues des taches et des resultats
        """
        self.task_queue = Queue()
        self.result_queue = Queue()

        self.register("get_task_queue", callable=lambda: self.task_queue)
        self.register("get_result_queue", callable=lambda: self.result_queue)
        super().__init__(address=("", port), authkey=key)
        self.server = self.get_server()
        self.server.serve_forever()


if __name__ == "__main__":
    # create a single QueueManager instance
    my_queue_manager = QueueManager()
