#Dictonaries are just like maps in other languages. They store key-value pairs, where each key is unique and maps to a specific value. Dictionaries are mutable, meaning you can change their content without changing their identity. But you can't have duplicates keys: each key needs to be ubiquitous within a dictionary.
#Dictionaries are defined using curly braces {} with key-value pairs separated by commas, and a colon separating keys and values.
#Examples:
#creating a dictionary
my_dict = {"name": "Heinthant", "age": 20, "city": "Bangkok"}
print(my_dict)  # Output: {'name': 'Heinthant', 'age': 20, 'city': 'Bangkok'}
#accessing values
print(my_dict["name"])  # Output: Heinthant
print(my_dict.get("age")) # Output: 20
#modifying values
my_dict["age"] = 21
print(my_dict)  # Output: {'name': 'Heinthant', 'age':
# 21, 'city': 'Bangkok'}
#adding key-value pairs
my_dict["job"] = "Developer"
print(my_dict)  # Output: {'name': 'Heinthant', 'age':
# 21, 'city': 'Bangkok', 'job': 'Developer'}
#removing key-value pairs
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Heinthant', 'age':
# 21, 'job': 'Developer'}
removed_value = my_dict.pop("job")
print(removed_value)  # Output: Developer
print(my_dict)  # Output: {'name': 'Heinthant', 'age':
# 21}
#dictionary methods
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age'])
values = my_dict.values()
print(values)  # Output: dict_values(['Heinthant', 21])
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Heinthant'), ('age', 21)])
#iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Heinthant
# age: 21
#nested dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(nested_dict["person1"]["name"])  # Output: Alice
#dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16
#Note: Dictionaries are unordered in versions before Python 3.7. From Python 3.7 onwards, they maintain insertion order. I'm using 3.12 so it's okay and ordered now. del keyword is a killer in all data structs in python because it can delete anything. .remove() is only for lists. .pop() works for both lists and dictionaries but in lists it removes by index while in dictionaries it removes by key. pop() remove the last item and return a value in lists but in dictionaries you have to specify the key to remove.