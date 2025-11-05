#Lambda Function Exercises(Implementing is hard af)
#Basic lambda
'''Task:
Given: students = [('Alice', 22), ('Bob', 25), ('Charlie', 20)]
Sort by age using a lambda as the key.'''
students = [('Alice', 22), ('Bob', 25), ('Charlie', 20)]
sorted_students = sorted(students, key= lambda x: x[1])
print(f"Sorted Students by Age: {sorted_students}")  # Output: Sorted Students by Age: [('Charlie', 20), ('Alice', 22), ('Bob', 25)]
#--------------------------------------------------------------------------------------------------
#Map and Filters wtih lambda funcs
'''Task:
Given a list of numbers, use:

map with a lambda to square each number.

filter with a lambda to keep only even squares.'''
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
even_squares = list(filter(lambda x: x%2 ==0, squared_numbers))
print(f"Squared Numbers: {squared_numbers}")  # Output: Squared Numbers: [1, 4, 9, 16, 25]
print(f"Even Squares: {even_squares}")      # Output: Even Squares: [4, 16]
#--------------------------------------------------------------------------------------------------
