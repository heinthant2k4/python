#Basics
#print "Hello" before the org_func
def decorator(func):
  def wrapper():
    print("Hello")
    func()
  return wrapper

@decorator
def say_name():
    print("Alex")

say_name()
# Output:
# Hello
# Alex
#---------------------------------------------------------------
# TODO: call func and return its result * 2
def decorator(func):
  def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        return result * 2
  return wrapper

@decorator
def add(a,b):
    return a + b

result = add(3,5)
print(f"Result: {result}")
# Output: Result: 16
#---------------------------------------------------------------
# TODO: print execution time of func
import time
def timer(func):
  def wrapper(*args, **kwargs):
      start = time.time()
      result = func(*args, **kwargs)
      end = time.time()
      print(f"Execution time: {end - start} seconds")
      return result
  return wrapper

@timer
def compute_sum(n):
    return sum(range(n))

compute_sum(1000000)
# Output: Execution time: 0.0098080 seconds (actual time may vary)
#---------------------------------------------------------------

#Arguments & Return Values
 # TODO: print the args and kwargs passed to func
def logger(func):
  def wrapper(*args, **kwargs):
      print(f"Arguments passed: {args}, {kwargs}")
      return func(*args, **kwargs)
  return wrapper

@logger
def org_func(a,b):
   return a+b

result = org_func(3,5)
print(f"Result: {result}")
# Output:
# Arguments passed: (3, 5), {}
# Result: 8
#---------------------------------------------------------------
 # TODO: prevent division by zero
def safe_divide(func):
  def wrapper(*args,**kwargs):
    if args[1] == 0:
          return "Error: Division by zero"
    return func(*args,**kwargs)
  return wrapper

@safe_divide
def divide(a,b):
    return a / b

result1 = divide(10,2)
print(f"10 / 2 = {result1}")
result2 = divide(10,0)
print(f"10 / 0 = {result2}")
# Output:
# 10 / 2 = 5.0
# 10 / 0 = Error: Division by zero
#---------------------------------------------------------------