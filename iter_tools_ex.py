import itertools
#Basic Itertools
'''Task:
Write a program that:

Takes a list of numbers [1, 2, 3]

Uses itertools.permutations to generate all permutations

Prints them as tuples.

Extension: Use itertools.combinations to get all 2-element combinations.'''
my_list = [1,2,3]
permutations = tuple(itertools.permutations(my_list))
print(f"Permutations: {permutations}")  # Output: Permutations: ((1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1))
combinations = tuple(itertools.combinations(my_list,2))
print(f"2-element Combinations: {combinations}")  # Output: 2-element Combinations: ((1, 2), (1, 3), (2, 3))
#-------------------------------------------------------------------------------------------------------
#Infinite Itertools
'''Task:
Use itertools.cycle to print “ON”, “OFF”, “ON”, “OFF” repeatedly until the user presses Ctrl+C.
Add a counter limit to break after 10 iterations safely.'''
cycler = itertools.cycle(['ON','OFF'])
print(f"Cycles: {[next(cycler) for _ in range(10)]}")  # Output: Cycles: ['ON', 'OFF', 'ON', 'OFF', 'ON', 'OFF', 'ON', 'OFF', 'ON', 'OFF']
#-------------------------------------------------------------------------------------------------------
#Data Chunking
'''Task:
Given a list of 20 elements, use itertools.islice to split it into chunks of 5.
No loops — only itertools!'''
data = list(range(1,21))
chunk_size = 5
chunks = [list(itertools.islice(data, i, i+chunk_size)) for i in range(0, len(data), chunk_size)]
#islice(iterable, start,stop) returns an iterator that produces selected elements from the input iterable, starting from the 'start' index up to, but not including, the 'stop' index.
#range is written in a way like in C,Java,etc where stop value is exclusive. for(i=0;i<len(data);i++)
#In this case, we start at index 0, stop point is data length, and step is the chunk_size which is 5.
print(f"Data Chunks: {chunks}")  # Output: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
#-------------------------------------------------------------------------------------------------------
#Running Totals
'''Task:
Given [10, 20, 30, 40], use itertools.accumulate to compute running totals.

Extension: Pass a custom lambda to accumulate that multiplies instead of adds.'''
numbers = [10,20,30,40]
running_totals = list(itertools.accumulate(numbers))
print(f"Running Totals: {running_totals}")  # Output: Running Totals: [10, 30, 60, 100]
running_products = list(itertools.accumulate(numbers, lambda x,y: x*y))
print(f"Running Products: {running_products}")  # Output: Running Products: [10, 200, 6000, 2400000]
#-------------------------------------------------------------------------------------------------------
#Cartesian Products
'''Task:
Generate all possible combinations of shirts (['red', 'blue']) and sizes (['S', 'M', 'L']) using itertools.product.'''
shirts = ['red','blue']
sizes = ['S','M','L']
product = list(itertools.product(shirts,sizes))
print(f"Shirt and Size Combinations: {product}")  # Output: Shirt and Size Combinations: [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
#-------------------------------------------------------------------------------------------------------