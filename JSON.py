#JSON module in Python helps alot when it comes to handling data in JSON format.
import json
# Example dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "Art"],
    "address": {
        "street": "123 Main St",
        "zip": "10001" 
    }
}
# Convert dictionary to JSON string(encode)
json_string = json.dumps(data,indent=None)
# Convert JSON string back to dictionary(decode)
data_parsed = json.loads(json_string)
print(f"\nParsed Dictionary:\n{data_parsed}")
# Accessing data from the parsed dictionary
print(f"\nName: {data_parsed['name']}")
print(f"Courses: {data_parsed['courses']}")
# Output:
# JSON String:
# {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "is_student": false,
#     "courses": [
#         "Math",
#         "Science",
#         "Art"
#     ],
#     "address": {
#         "street": "123 Main St",
#         "zip": "10001"
#     }
# }
# Parsed Dictionary:
# {'name': 'Alice', 'age': 30, 'city': 'New York', 'is_student': False, 'courses': ['Math', 'Science', 'Art'], 'address': {'street': '123 Main St', 'zip': '10001'}}
# Name: Alice
# Courses: ['Math', 'Science', 'Art']
#---------------------------------------------------------------
#Note: JSON module is very useful for web development and data interchange between systems.