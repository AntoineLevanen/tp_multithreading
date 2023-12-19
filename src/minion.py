#!/usr/bin/env python3

from manager import QueueClient


class Minion(QueueClient):
    def __init__(self):
        pass
        """
        regarde si une tache est dispo, et l'execute
        Queue.get()

        avec le resultat,
        Queue.put(resultat)
        """
        self.task

    def getTask(self):
        # si la file de tache a realier n'est pas vide
        if not self.task_queue_ref.empty():
            self.task = self.result_queue_ref.get()

    def work(self):
        result = self.task.work()
        self.result_queue_ref.put(result)


if __name__ == "__main__":
    minion = Minion()
