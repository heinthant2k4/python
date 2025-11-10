#Process and Thread are different concepts in programming, particularly in the context of concurrent execution.
#Process: A process is an independent program in execution, with its own memory space. Each process has its own
# resources and operates independently of other processes. Communication between processes typically requires
# inter-process communication (IPC) mechanisms.
#Thread: A thread is a smaller unit of execution within a process. Multiple threads within the same process share the same
# memory space and resources, allowing for easier communication and data sharing.
#Threads are often used to perform tasks concurrently within a single process, improving efficiency and responsiveness.
#Example of threading in Python
import threading
import time
def print_nums():
  for i in range(1,6):
    print(i)
    time.sleep(1)

def print_letters():
  for letter in ['A','B','C','D','E']:
    print(letter)
    time.sleep(1)
# Create threads
num_thread = threading.Thread(target=print_nums)
letter_thread = threading.Thread(target=print_letters)
# Start threads
num_thread.start()
letter_thread.start()
# Wait for both threads to complete
num_thread.join()
letter_thread.join()
print("Both threads have finished execution.")
# Output:
# 1
# A
# 2
# B
# 3
# C
# 4
# D
# 5
# E
# Both threads have finished execution.
#---------------------------------------------------------------
#Example of threading with arguments
def print_range(start,end):
  for i in range(start,end+1):
    print(i)
    time.sleep(0.5)

#creating threads
thread_1 = threading.Thread(target=print_range, args=(1,5))
thread_2 = threading.Thread(target=print_range, args=(6,10))
#starting threads
thread_1.start()
thread_2.start()
#waiting for threads to complete
thread_1.join()
thread_2.join()
print("Range printing completed.")
# Output:
# 1
# 6
# 2
# 7
# 3
# 8
# 4
# 9
# 5
# 10
# Range printing completed.
#---------------------------------------------------------------
#Multithreading: Using multiple threads to perform tasks concurrently
def student(id):
  print(f"Student {id} is starting an assignment.")
  time.sleep(2)
  print(f"Student {id} has completed the assignment.")

#creating multiple threads for students
threads = []
for i in range(1,4):
  t = threading.Thread(target=student, args=(i,))
  threads.apeend(t)
  t.start()
#waiting for all threads to complete
for t in threads:
  t.join()
print("All students have completed their assignments.")
# Output:
# Student 1 is starting an assignment.
# Student 2 is starting an assignment.
# Student 3 is starting an assignment.
# Student 1 has completed the assignment.
# Student 2 has completed the assignment.
# Student 3 has completed the assignment.
# All students have completed their assignments.
#---------------------------------------------------------------
#Notes: Threads share the same memory space within a process, making data sharing easier but requiring careful synchronization to avoid conflicts.
# Use threading for I/O-bound tasks to improve performance
# Avoid using threading for CPU-bound tasks due to Python's Global Interpreter Lock (GIL)
# Always ensure threads are properly managed to prevent resource leaks or deadlocks.
#---------------------------------------------------------------
#CPU-bound vs I/O-bound tasks
#CPU-bound tasks are limited by the speed of the CPU, while I/O-bound tasks are limited by input/output operations.
#Example of CPU-bound task
def cpu_bound_task(n):
  result = 0
  for i in range(n):
    result += i*i
  return result
#Example of I/O-bound task
def io_bound_task():
  time.sleep(2)  # Simulating an I/O operation with sleep
  return "I/O task completed"
#In general, use threading for I/O-bound tasks to improve performance, while CPU-bound tasks may benefit more from multiprocessing. Any tasks that involve waiting for external resources, such as file reading/writing or network requests, are typically I/O-bound. And those that require intensive computations, such as mathematical calculations or data processing, are CPU-bound.