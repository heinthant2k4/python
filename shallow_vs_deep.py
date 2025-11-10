#Shallow Vs Deep Copy in Python: 
#In python assigning a variable to another variable using "=" creates a reference to the original object (shallow copy).
#To create a deep copy (a new object with its own memory space), we can use the copy module's deepcopy() function.
#Shallow copy or assignments just point to the same memory location, so changes to one will affect the other.
#Deep copy creates a new object, so changes to one do not affect the other.
#Useful when dealing with mutable objects like lists or dictionaries, especially when they contain nested objects.
import copy
#Shallow Copy Example
original_list = [1,2,3]
shallow = copy.copy(original_list)
shallow.append(4)
print("Original List after shallow copy modification:", original_list) # Output: [1, 2, 3]
print("Shallow Copy:", shallow) # Output: [1, 2, 3, 4]
#Deep Copy Example
original_list2 = [1,2,3]
deep = copy.deepcopy(original_list2)
deep.append(4)
print("Original List after deep copy modification:", original_list2) # Output: [1, 2, 3]
print("Deep Copy:", deep) # Output: [1, 2, 3, 4]
#Note: For nested objects, shallow copy only copies the references of inner objects, while deep copy creates new inner objects as well.
nested_list = [[1,2],[3,4]]
shallow_nested = copy.copy(nested_list)
deep_nested = copy.deepcopy(nested_list)
shallow_nested[0].append(5)
deep_nested[1].append(6)
print("Original Nested List after shallow copy modification:", nested_list) # Output: [[1, 2, 5], [3, 4]]
print("Shallow Nested Copy:", shallow_nested) # Output: [[1, 2, 5], [3, 4]]
print("Deep Nested Copy:", deep_nested) # Output: [[1, 2], [3, 4, 6]]
#In summary, use shallow copy for simple objects and deep copy for complex, nested objects to avoid unintended side effects.
#---------------------------------------------------------------