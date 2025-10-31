#Sets are unordered collections of unique elements in Python. They are useful for storing items where duplicates are not allowed and for performing mathematical set operations like union, intersection, and difference.
#Sets are defined using curly braces {} or the set() constructor.
#Examples:
#creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
#creating a set using set() constructor
another_set = set([4, 5, 6, 7, 8])
print(another_set)  # Output: {4, 5, 6, 7, 8}
#adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
#removing elements
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}
#discarding elements (does not raise an error if the element is not found)
my_set.discard(10)  # No error
print(my_set)  # Output: {1, 2, 4, 5, 6}
#set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
#union
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}
#intersection
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3, 4}
#difference
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}
#symmetric difference
sym_diff_set = set_a.symmetric_difference(set_b)
print(sym_diff_set)  # Output: {1, 2, 5, 6}
#checking membership
print(2 in set_a)  # Output: True
print(5 in set_a)  # Output: False
#iterating through a set
for item in my_set:
    print(item)
# Output:
# 1
# 2
# 4
# 5
# 6
#set comprehension
squared_set = {x**2 for x in range(6)}
print(squared_set)  # Output: {0, 1, 4, 9, 16, 25} 

#Note: Sets are unordered, so the elements may appear in a different order when printed. 0 and False are the same and duplicates are not allowed in sets. 1 and True are also the same in sets.