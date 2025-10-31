#access list items
my_list = [10, 20, 30, 40, 50]
first_item = my_list[0]
last_item = my_list[-1]
print(f"First item: {first_item}, Last item: {last_item}")  #
# Output: First item: 10, Last item: 50
#slicing lists
sublist = my_list[1:4]
print(f"Sublist: {sublist}")  # Output: Sublist: [20, 30, 40]

#modifying lists
my_list[2] = 35
print(f"Modified list: {my_list}")  # Output: Modified list: [10
#, 20, 35, 40, 50]

#adding elements
my_list.append(60)
print(f"List after append: {my_list}")  # Output: List after append: [10, 20, 35,
# 40, 50, 60]
my_list.insert(2, 25)
print(f"List after insert: {my_list}")  # Output: List after insert: [10, 20, 25, 35,
# 40, 50, 60]