#!/usr/bin/env python3
import json
from time import perf_counter

import numpy as np


class Task:
    def __init__(self, identifier: int, size: int, a=None, b=None, x=None, time=None):
        self.identifier = identifier
        self.size = size
        if a is None:
            self.a = np.random.rand(size, size)
            self.b = np.random.rand(
                size,
            )
            self.x = np.zeros((size,))
            self.time = 0.0
        else:
            self.identifier = identifier
            self.a = a
            self.b = b
            self.x = x
            self.time = time

    def work(self) -> float:
        time_start = perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        time_end = perf_counter()
        self.time = time_end - time_start
        return self.time

    def to_json(self) -> str:
        return json.dumps(
            {
                "id": self.identifier,
                "size": self.size,
                "a": self.a.tolist(),
                "b": self.b.tolist(),
                "x": self.x.tolist(),
                "time": self.time,
            },
            separators=(",", ":"),
        )

    @classmethod
    def from_json(cls, text: str) -> "Task":
        values = json.loads(text)
        return Task(
            identifier=values["id"],
            size=values["size"],
            a=values["a"],
            b=values["b"],
            x=values["x"],
            time=values["time"],
        )

    def __eq__(self, other: "Task") -> bool:
        return (
            self.identifier is other.identifier
            and self.size is other.size
            and np.array_equal(self.a, np.array(other.a))
            and np.array_equal(self.b, np.array(other.b))
            and np.array_equal(self.x, np.array(other.x))
            and self.time == other.time
        )


def test_task():
    task_1 = Task(1, 2)
    text = task_1.to_json()
    task_2 = Task.from_json(text)
    print(task_1 == task_2)


if __name__ == "__main__":
    # ma_tache = Task(0, 3)
    # print(ma_tache.work())
    test_task()
