#List is like an array in C/C++, they are mutable,ordered collection of items.
#They are defined using square brackets [] and items are separated by commas.
#Lists can contain items of different data types including other lists.
#Lists support indexing and slicing to access individual elements or sublists.
#Lists have various built-in methods for adding, removing, and manipulating items.
#Examples:
#creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
#accessing elements
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: cherry
#slicing
print(fruits[1:3]) # Output: ['banana', 'cherry']
#modifying elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
#adding elements
fruits.append("date")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry',
# 'date']
#removing elements
fruits.remove("apple")
print(fruits)  # Output: ['blueberry', 'cherry', 'date']
#list methods
fruits.sort()
print(fruits)  # Output: ['blueberry', 'cherry', 'date']
fruits.reverse()
print(fruits)  # Output: ['date', 'cherry', 'blueberry']
length = len(fruits)
print(length)  # Output: 3

#using lists like stacks and queues
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # Output: [1, 2, 3]
stack.pop()
print(stack)  # Output: [1, 2]

#queue using list
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # Output: deque([1, 2, 3])
queue.popleft()
print(queue)  # Output: deque([2, 3])

#nested lists
matrix = [[1,2,3],[4,5,6],[7,8,9]] #3x3 matrix
print(matrix[0])    # Output: [1, 2, 3]
print(matrix[1][2]) # Output: 6
#iterating through a list
for fruit in fruits:
    print(fruit)
# Output:
# date
# cherry
# blueberry

#list comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
#filtering with list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

#nested list comprehension
matrix_transpose = [[row[i] for row in matrix] for i in range(3)]
print(matrix_transpose)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
