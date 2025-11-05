#Strings are more than an array of characters in Python. They are immutable sequences used to store text data. Strings can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """) for multi-line strings.
#Examples:
#creating strings
single_quote_str = 'Hello, World!'
double_quote_str = "Hello, Python!"
triple_quote_str = '''This is a
multi-line string.'''
print(single_quote_str)  # Output: Hello, World!
print(double_quote_str)  # Output: Hello, Python!
print(triple_quote_str)
# Output:
# This is a
# multi-line string.
#string indexing and slicing
sample_str = "Python"
print(sample_str[0])  # Output: P
print(sample_str[-1])  # Output: n
print(sample_str[1:4])  # Output: ython
print(sample_str[:3])  # Output: Pyt
print(sample_str[3:])  # Output: hon
#string methods
upper_str = sample_str.upper()
print(upper_str)  # Output: PYTHON
lower_str = sample_str.lower()
print(lower_str)  # Output: python
split_str = "Hello, World!".split(", ")
print(split_str)  # Output: ['Hello', 'World!']
joined_str = " ".join(["Hello", "Python"])
print(joined_str)  # Output: Hello Python
replace_str = sample_str.replace("Py", "Ja")
print(replace_str)  # Output: Jathon
#string formatting
name = "Heinthant"
age = 20
formatted_str = f"My name is {name} and I am {age} years old." #f" " f before the string to use variables directly
print(formatted_str)  # Output: My name is Heinthant and I am 20 years old.
#escape sequences
escape_str = "He said, \"Hello!\"\nWelcome to Python programming."
print(escape_str)
# Output:
# He said, "Hello!"
# Welcome to Python programming.
#raw strings (ignores escape sequences)
raw_str = r"C:\Users\Heinthant\Documents"
print(raw_str)  # Output: C:\Users\Heinthant\Documents
#string concatenation
str1 = "Hello"
str2 = "World"
concat_str = str1 + ", " + str2 + "!"
print(concat_str)  # Output: Hello, World!
#string repetition
repeat_str = "Ha" * 3
print(repeat_str)  # Output: HaHaHa
#checking membership
print("Py" in sample_str)  # Output: True
print("Java" in sample_str)  # Output: False
#iterating through a string
for char in sample_str:
    print(char)
# Output:
# P
# y
# t
# h
# o
# n
#Note: Strings are immutable, so any operation that modifies a string will create a new string rather than changing the original string.