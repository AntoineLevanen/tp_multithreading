#!/usr/bin/env python3
import time

from manager import QueueClient
from task import Task


class Boss(QueueClient):
    """
    cree une tache et la met dans task_queue,
    instancie la class tache
    Queue.put(une_tache)
    """

    def __init__(
        self,
    ):
        super().__init__()

    def addElement(self, id, size):
        my_task = Task(id, size)
        self.task_queue.put(my_task)


if __name__ == "__main__":
    boss = Boss()
    boss.addElement(time.time(), 3000)
