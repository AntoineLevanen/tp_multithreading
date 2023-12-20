# tp_multithreading

## dependencies
- python 3
- numpy


## get the project
create a python virtual environment
```
python3 -m venv .venv
```
then activate the environment
```
source .venv/bin/activate
```
make sure pip is install
```
pip install -U pip
```
then install numpy
```
pip install -U numpy
```

## file structure

### src/manager.py
Define a BaseManager to manage Python Queues

### src/boss.py
Boos class that make jobs and put them in the corresponding queue

### src/minion.py
Minion class that take a job, execute the job and put the time taken by the job in a result queue

### src/task.py
Task class that resolve a linear problem (the goal here is to make a task that take time for test purpose)

### src/proxy.py
