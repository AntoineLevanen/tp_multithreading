#!/usr/bin/env python3
import multiprocessing
from multiprocessing import Queue


class QueueClient:
    def __init__(self):
        pass


class QueueManager(multiprocessing.managers.BaseManager):
    def __init__(self):
        """
        Contient les Queues des taches et des resultats
        """
        self.task_queue = Queue()
        self.result_queue = Queue()


if __name__ == "__main__":
    pass
