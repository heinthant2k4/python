#Tuples
# Given:
data = ('Alice', 25, 'Engineer')
# Task: Unpack the tuple into three variables and print:
# "Alice is a 25-year-old Engineer"
name, age, career = data
print(f"{name} is a {age}-year-old {career}")
# Output: Alice is a 25-year-old Engineer
#---------------------------------------------------------------
nums = (10, 20, 30, 40, 50)
# Task: Print the first two and last two elements using slicing
first_two = data[:2]
last_two = data[-2]
# Output:
# First two elements: (10, 20)
# Last two elements: (40, 50)
#---------------------------------------------------------------
t = (1, 2, 3)
# Task: Try to change the second element to 99.
# What happens? How can you create a new tuple with the updated value?
# t[1] = 99 <-- this would be an error since tuples are immutable.
#Creating a new tuple is the best choice.
t = (t[0],99,t[2])
print(f"Updated tuple: {t}")
# Output: Updated tuple: (1, 99, 3)
#---------------------------------------------------------------
################################################################
#Dictonaries
student = {'name': 'John', 'age': 21, 'grade': 'A'}
# Task: Print only the keys, then only the values
print(f"Keys: {student.keys()}")
print(f"Values: {student.values}")
# Output:
# Keys: dict_keys(['name', 'age', 'grade'])
# Values: dict_values(['John', 21, 'A'])
#---------------------------------------------------------------
scores = {'Math': 90, 'Science': 85}
# Task: Add 'English': 88, and update 'Science' to 89
#This is a dictonary so I can mutate this.
scores['English'] = 88
scores['Science'] = 89
print(f"Updated scores: {scores}")
# Output: Updated scores: {'Math': 90, 'Science': 89, 'Englisy': 88}
#---------------------------------------------------------------
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
# Task: Given 'yellow', find which fruit(s) have that color
target = "yellow"
fruits = [fruit for fruit,color in fruit_colors.items() if color == target]
print("Fruits with color yellow:", fruits)
# Output: Fruits with color yellow: ['banana']
#---------------------------------------------------------------
################################################################
#Collections
from collections import Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# Task: Use Counter to find the two most common fruits
fruit_counter = Counter(words)
most_common_two = fruit_counter.most_common(2)
# Output: Two most common fruits: [('apple', 3), ('banana', 2)]
#---------------------------------------------------------------
from collections import deque
# Task: Create a deque, add elements to both ends, and remove one from the front
my_deque = deque([1,2,3])
my_deque.append(4)      # Add to the right
my_deque.appendleft(0)  # Add to the left
print("Deque after appends:", my_deque)
my_deque.popleft()      # Remove from the left
my_deque.pop()          # Remove from the right
print("Deque after pops:", my_deque)
# Output:
# Deque after appends: deque([0, 1, 2, 3, 4])
# Deque after pops: deque([1, 2, 3])
#---------------------------------------------------------------
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
# Task: Create a Point instance and print its coordinates
#eg: 3,4 and its x and y
pts = Point(3,4)
print(f"Point coordinates: x={pts.x}, y={pts.y}")
# Output: Point coordinates: x=3, y=4
#---------------------------------------------------------------
#Lists
nums = [1, 2, 3, 4, 5]
# Task: Create a new list containing squares of even numbers only
squared_evens = [x**2 for x in nums if x % 2 ==0]
print("Squared even numbers:", squared_evens)
# Output: Squared even numbers: [4, 16]
#---------------------------------------------------------------
names = ['Zoe', 'alex', 'John', 'mike']
# Task: Sort alphabetically (case-insensitive)
sorted_names = sorted(names, key= lambda x: x.lower())
# Output: Sorted names: ['alex', 'John', 'mike', 'Zoe']
#---------------------------------------------------------------
matrix = [[1, 2], [3, 4], [5, 6]]
# Task: Flatten the matrix into [1, 2, 3, 4, 5, 6]
flattened_matrix = [num for row in matrix for num in row]
print("Flattened matrix:", flattened_matrix)
# Output: Flattened matrix: [1, 2, 3, 4, 5, 6]
#---------------------------------------------------------------