# tp_multithreading
This project is the realization of practical class to learn multithreading (and git) using Python and C++.

## dependencies
- Python
    - python 3
    - numpy
- C++
    - dependencies are downloaded with CMakeLists.txt


## get the project
Create a python virtual environment
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
Enable the python `task_queue` to be acceced via a http request.

### src/low_level.cpp
A C++ class that get a task on `task_queue` via a http request, then parse the data and solve the problem.

## Execute Python part
Launch only one manager `python src/manager.py`.
Launch a boss to add one task in the queue `python src/boss.py`.
Launch as many minions as you want `python src/minion.py`.

## Execute C++ part
Launch only one manager `python src/manager.py`.
Launch a boss to add one task in the queue `python src/boss.py`.
Launch only one proxy `python src/proxy.py`.
You can get the first task in the queue by accessing it via a web browser with `htts://localhost:8000`.
Or use `$ curl https://localhost:8000`.


## Complile the project
List of compilation flags that can be used with g++ :
- -o0
- -os to minimize the size of executable file
- -o1
- -o2 (many software are compiled with that)
- ...
- -o9

To build the project with cmake:
Use `cmake -B build -S .` to build the dependencies, then `cmake --build build`, finaly execute the program with `./build/low_level`.

Or use `$ cmake -B build-deb -S . -DCMAKE_BUILD_TYPE=Debug` to build the dependencies, then `cmake --build build-deb`, finaly execute the program with `./build-deb/low_level` using debug config.

Or use `$ cmake -B build-rel -S . -DCMAKE_BUILD_TYPE=Release` to build the dependencies, then `cmake --build build-rel`, finaly execute the program with `./build-rel/low_level` by removing all debug information in the executable file.


## Result
Time taken to execute the task for a problem of size 3000 :
- Python
    - mean time over 5 executions : 0.444565 seconds
- C++ using Eigen colPivHouseholderQr() solver :
    - mean time over 5 executions : 16.92968 seconds
- C++ using Eigen lu() solver :
    - mean time using 1 core over 5 executions : 1.496276 seconds
    - mean time using 2 core over 5 executions : 1.039027 seconds
    - mean time using 4 core over 5 executions : 0.794219 seconds

## TODO
Send the result of the C++ work back to the `result_queue` in Python.
