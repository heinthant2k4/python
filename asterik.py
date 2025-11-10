#Asterik operators when used as prefix to a parameter in function definition, it allows the function to accept an arbitrary number of positional arguments as a tuple.
#When used as prefix to a parameter in function call, it unpacks a list or tuple into positional arguments.
#Similarly, double asterik (**) when used as prefix to a parameter in function definition, it allows the function to accept an arbitrary number of keyword arguments as a dictionary.
#unpacking
def example_function(*args, **kwargs):
    print("Function executed")
    print(args[0])  # Accessing first positional argument
    print(kwargs.get('key1'))  # Accessing keyword argument with key 'key1'

example_function(1,2,3,key1="val1", key2="val2")#in this case args is (1,2,3)[tuple] and kwargs is {'key1':'val1','key2':'val2'}[dict] using * and ** to pack them respectively
# Output:
# Function executed
# 1
# val1
#---------------------------------------------------------------
nums = (1,2,3,4)
print(*nums)#unpacking nums tuple into positional arguments
# Output: 1 2 3 4
for i in len(nums):
    print(nums[i])
# Output:
# 1
# 2
# 3
# 4
#---------------------------------------------------------------
keywords = {'a':10,'b':20}
print(**keywords)#unpacking keywords dict into keyword arguments
# Output: a=10 b=20
for i in len(keywords):
    print(f"{i}={keywords[i]}")
# Output:
# a=10
# b=20
#---------------------------------------------------------------
