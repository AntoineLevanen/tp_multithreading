#!/usr/bin/env python3

from manager import QueueClient


class Minion(QueueClient):
    def __init__(self):
        super().__init__()

    def getTask(self):
        #
        while True:
            # if the queue is not empty
            if self.task_queue.empty():
                print("No task to process...")
                break
            # else get a job
            task = self.task_queue.get()
            # process the job
            process_time = task.work()
            print(process_time)
            # put the result in the result queue
            self.result_queue.put(process_time)


if __name__ == "__main__":
    minion = Minion()
    minion.getTask()
