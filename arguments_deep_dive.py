#Arguments in functions are more than just def func(a,b). They can be positional,keyword,default,var-positional,var-keyword.
#Return values can also be multiple, unpacked,or ignored.
#Understanding these concepts deeply can help in writing flexible and reusable code.
#postitional examples:
def sum(a,b):
  return a + b

result = sum(3,5)
print(f"Sum: {result}")
# Output: Sum: 8
#---------------------------------------------------------------
#keywords
def greet(name, greeting):
  return f"{greeting}, {name}!"

message = greet(name="Hein", greeting="Mingalarbar")
print(message)
# Output: Mingalarbar, Hein!
#---------------------------------------------------------------
#default arguments
def power(base, exponent=2):
  return base ** exponent
squares = []
for _ in range(4):
  squares.append(power(_,))#We didn't provide exponent, so default 2 is used
print(f"Squares: {squares}")
# Output: Squares: [0, 1, 4, 9]
#---------------------------------------------------------------
#var-positional (*args), we have seen this in decorators with *args and **kwargs in wrapper functions
def multiply(*args):
  result = 1
  for num in args:
    result *= num
  return result
product = multiply(2,3,4)#now (2,3,4) is an tuple assigned to args
print(f"Product: {product}")
# Output: Product: 24
#---------------------------------------------------------------
#var-keyword (**kwargs)
def build_profile(**kwargs):
  profile = {}#empty dict
  for key,value in kwargs.items():#kwargs is a dict of passed key-value pairs
    profile[key] = value
  return profile

user_profile = build_profile(name="Thakhin Gyi", age=69, city="Meiktila")
print(f"User Profile: {user_profile}")
# Output: User Profile: {'name': 'Thakhin Gyi', 'age': 69, 'city': 'Meiktila'}
#---------------------------------------------------------------