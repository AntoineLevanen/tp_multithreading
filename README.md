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
Boss class that make jobs and put them in the corresponding queue

### src/minion.py
Minion class that take a job, execute the job and put the time taken by the job in a result queue

### src/task.py
Task class that resolve a linear problem (the goal here is to make a task that take time for test purpose)

### src/proxy.py


## Execute Python part
Launch only one manager `python src/manager.py`.
Launch only one boss `python src/boss.py`.
Launch as many minions as you want `python src/minion.py`.

## Execute C++ part
Launch only one manager `python src/manager.py`.
Launch only one boss `python src/boss.py`.
Launch only one proxy `python src/proxy.py`.
You can get the first task in the queue by accessing it via a web browser with `htts://localhost:8000`.
Or use `$ curl https://localhost:8000`.
