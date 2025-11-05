#Collections in Python
#Collections are data structures that can hold multiple items. Python provides several built-in collection types, including lists, tuples, sets, and dictionaries. Each collection type has its own characteristics and use cases. Exploring these collection types will help you understand how to store and manipulate groups of data effectively. This is focused on using the modules related to collections in Python. We can create deques, linked lits, ordered dicts, default dicts, counters, named tuples, etc. using the collections module.
#Examples:
import collections
#creating a deque (double-ended queue)
my_deque = collections.deque([1,2,3])
print(my_deque)  # Output: deque([1, 2, 3])
#adding elements to the right
my_deque.append(4)
print(my_deque)  # Output: deque([1, 2, 3, 4])
#adding elements to the left
my_deque.appendleft(0)
print(my_deque)  # Output: deque([0, 1, 2, 3, 4])
#removing elements from the right
my_deque.pop()
print(my_deque)  # Output: deque([0, 1, 2, 3])
#removing elements from the left
my_deque.popleft()
print(my_deque)  # Output: deque([1, 2, 3])
#creating an ordered dictionary
ordered_dict = collections.OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#creating a default dictionary
default_dict = collections.defaultdict(int)
default_dict['a'] += 1
default_dict['b'] += 2
print(default_dict)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
#creating a counter
my_counter = collections.Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(my_counter)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})
#creating a named tuple
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p)  # Output: Point(x=10, y=20)
print(p.x)  # Output: 10
print(p.y)  # Output: 20
#Note: The collections module provides specialized container datatypes that can be very useful for certain applications. Deques are optimized for fast appends and pops from both ends, making them ideal for queues and stacks. OrderedDict maintains the order of keys based on insertion order (note: from Python 3.7 onwards, regular dicts also maintain insertion order). DefaultDict simplifies handling missing keys by providing default values. Counter is great for counting hashable objects, and NamedTuple allows for creating