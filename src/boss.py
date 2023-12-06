#!/usr/bin/env python3

from manager import QueueClient


class Boss(QueueClient):
    def __init__(self):
        pass
        """
        cree une tache et la met dans task_queue,
        instancie la class tache
        Queue.put(une_tache)
        """


if __name__ == "__main__":
    boss = Boss()
