#Lambda function is an anonymous function in Python that can take any number of arguments but can only have one expression.
#They are often used for short, throwaway functions that are not going to be reused elsewhere in the code. They are defined using the lambda keyword followed by the arguments, a colon, and the expression.
#Examples:
#simple lambda function that adds two numbers
add = lambda x,y: x+y
print(add(5,3))  # Output: 8
#lambda function with no arguments
greet= lambda : "Hello There!"
print(greet())  # Output: Hello There!
#lambda function with multiple arguments
multiply = lambda a,b,c: a*b*c
print(multiply(2,3,4))  # Output: 24
#using lambda with map() to square each number in a list
numbers = [1,2,3,4,5]
squared_num = list(map(lambda x: x**2, numbers))
print(squared_num)  # Output: [1, 4, 9, 16, 25]
#using lambda with filter() to get even numbers from a list
even_num = list(filter(lambda x: x%2==0, numbers))
print(even_num)  # Output: [2, 4]
#using lambda with sorted() to sort a list of tuples based on the second element
tuples_list = [(1,3), (2,1), (4,2)]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(2, 1), (4, 2), (1, 3)]
#Note: While lambda functions can be useful for simple tasks, they are limited to a single expression and can sometimes make code less readable if overused or used for complex operations. For more complex functions, it's often better to define a regular function using the def keyword.