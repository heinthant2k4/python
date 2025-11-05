#Exceptions and Error handling in Python rely on the use of try, except, else, and finally blocks to manage and respond to runtime errors in a controlled manner.
#Examples:
#try and except
try:
  result = 10 / 0
except ZeroDivisionError:
  print("Error: Division by zero is not allowed.")  # Output: Error: Division by zero is not allowed.
#try, except and else
try:
  result = 10 / 2
except ZeroDivisionError:
  print("Error: Division by zero is not allowed.")
else:
  print(f"Result is {result}")  # Output: Result is 5.0
#try, except and finally
try:
  file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
  print("Error: File not found.")  # Output: Error: File not found.
finally:
  print("Execution completed.")  # Output: Execution completed.

#Multiple except blocks
try:
  number = int(input("Enter a number:"))
  result = 10 / number
except ZeroDivisionError:
  print("Error: Division by zero is not allowed.")  # Output: Error: Division by zero is not allowed.
except ValueError:
  print("Error: Invalid input. Please enter a valid integer.")  # Output: Error: Invalid input. Please enter a valid integer.
except Exception as e:
  print(f"An unexpected error occurred: {e}")
else:
  print(f"Result is {result}") # Output: Result is 5.0 (if valid input is given)

#Raising exceptions
def check_positive(num):
  if num < 0:
    raise ValueError("Negative value error: Number must be positive.")
  return num
try:
  print(check_positive(-5))
except ValueError as ve:
  print(ve)  # Output: Negative value error: Number must be positive.

#Custom exception
class CustomError(Exception):
  pass
def risky_function():
  raise CustomError("This is a custom error message.")
try:
  risky_function()
except CustomError as ce:
  print(ce)  # Output: This is a custom error message.

#Note: Proper exception handling is crucial for building robust applications. It allows developers to anticipate potential errors and handle them gracefully, ensuring that the program can recover or fail safely without crashing unexpectedly.