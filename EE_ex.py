#Basic try/except
'''Write a function that divides two numbers.
Catch:

ZeroDivisionError

TypeError
and print user-friendly messages.'''
def divide_nums(num1, num2):
  try:
    result = num1/num2
  except ZeroDivisionError:
    print("Error: You can't divide by zero!")
  except TypeError:
    print("Error: Please provide numbers only!")
  else:
    print(f"The result is: {result}")
# Test cases
divide_nums(10, 2)  # Valid case
divide_nums(10, 0)  # ZeroDivisionError case
divide_nums(10, 'a')  # TypeError case
#----------------------------------------------------------------------------------------------------
#Multiple exceptions
'''Task:
Ask the user for a number input, and handle:

ValueError (non-numeric input)

KeyboardInterrupt (user presses Ctrl+C)'''
def get_number():
  try:
    input_val = input("Please enter a number: ")
    number = float(input_val)
  except ValueError:
    print("Error: That's not a valid number!")
  except KeyboardInterrupt:
    print("\nProcess interrupted by user.")
#-------------------------------------------------------------------------------------------------------
