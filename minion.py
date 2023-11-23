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


if __name__ == "__main__":
    minion = Minion()
