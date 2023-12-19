#!/usr/bin/env python3

from manager import QueueClient
from task import Task


class Boss(QueueClient):
    """
    cree une tache et la met dans task_queue,
    instancie la class tache
    Queue.put(une_tache)
    """

    def __init__(self, task_size):
        self.task_size = task_size

    def addElement(self):
        my_task = Task(self.task_size)
        self.task_queue_ref.put(my_task)


if __name__ == "__main__":
    boss = Boss()
