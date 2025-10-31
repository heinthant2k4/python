#Tuples are the same as lists but they are immutable (cannot be changed)
#Examples:
#creating a tuple
my_tuple = (1,2,3,4,5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
#accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[-1]) # Output: 5
#slicing
print(my_tuple[1:4]) # Output: (2, 3, 4

#tuples are immutable
#my_tuple[1] = 10  # This will raise a TypeError
#tuple methods
length = len(my_tuple)
print(length)  # Output: 5
count_of_2 = my_tuple.count(2)
print(count_of_2)  # Output: 1
index_of_3 = my_tuple.index(3)
print(index_of_3)  # Output: 2
#single element tuple
single_element_tuple = (10,)
print(single_element_tuple)  # Output: (10,)
#tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5
#nested tuples
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1])    # Output: (2, 3)
print(nested_tuple[1][0]) # Output: 2

#iterating through a tuple
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3
# 4
# 5

#tuple comprehension (using generator expression)
squares = tuple(x**2 for x in range(5))
print(squares)  # Output: (0, 1, 4, 9, 16)
#Note: Tuples are generally faster than lists and are used when immutability is required.