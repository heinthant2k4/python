#Generator is a type of function that can act as an iterator(can be used in a for loop). We can use return or yield statement to return values from a generator function. The difference is that return statement returns a single value and terminates the function, whereas yield statement returns a value and pauses the function, allowing it to be resumed later to produce a series of values over time. Return is like emptying a bucket and yield is like a tap that gives water when needed. Useful when reading large files or data streams.
#Examples
def count_up_to(n):#Generator func
  count = 1
  while count <= n:
    yield count
    count+=1

counter = count_up_to(5)
for num in counter:
  print(num)
# Output:
# 1
# 2
# 3
# 4
# 5
#---------------------------------------------------------------
def fibonacci_sequence(n):#Generator func
  a,b = 0,1
  for x in range(n):
    yield a
    a,b = b, b+1

fib = fibonacci_sequence(6)
for num in fib:
  print(num)
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
#---------------------------------------------------------------
#Task: Create a generator that yields even numbers up to n
def even_numbers(n):
  for num in range(2, n+1, 2):
    yield num

evens = even_numbers(5)
for even in evens:
  print(even)
# Output:
# 2
# 4
# 6
# 8
# 10
#---------------------------------------------------------------
#Task: Create a generator that yields the characters of a string one by one
def char_gen(s):
  for char in s:
    yield char
  
chars = char_gen("Lee Pal")
for c in chars:
  print(c)
# Output:
# L
# e
# e
#
# P
# a
# l
#---------------------------------------------------------------
#Note: Generators are memory efficient and useful for handling large datasets or streams of data where
#you don't want to load everything into memory at once.
#They provide a way to produce values on-the-fly and can be iterated over just like lists or other iterables.
#Generators can also be created using generator expressions, which are similar to list comprehensions but use parentheses instead of square brackets.
#Example of generator expression:
squared_gen = (x**2 for x in range(5))
for square in squared_gen:
  print(square)
# Output:
# 0
# 1
# 4
# 9
# 16
#---------------------------------------------------------------