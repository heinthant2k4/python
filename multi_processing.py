#Multiprocessing in python is a module that allows the creation of multiple processes, enabling parallel execution of tasks to improve performance on multi-core systems. It provides an interface similar to the threading module but uses separate memory space for each process, avoiding issues with the Global Interpreter Lock (GIL) in CPython. Typically used for CPU-bound tasks.
import multiprocessing
import time
# Function to be executed in a separate process
def worker(num):
  print(f"Worker {num} is starting.")
  time.sleep(2)
  print(f"Worker {num} has finished.")
# Creating processes
processes = []
for i in range(3):
  p = multiprocessing.Process(target=worker, args=(i,))
  processes.append(p)
  p.start()
  #waiting for proccesing to finish
  p.join()
print("All workers have finished execution.")
# Output:
# Worker 0 is starting.
# Worker 0 has finished.
# Worker 1 is starting.
# Worker 1 has finished.
# Worker 2 is starting.
# Worker 2 has finished.
# All workers have finished execution.
#---------------------------------------------------------------