#Itertools are a set of function modules that allows us to work with iterators to produce complex iterators. Can be used to create efficient loops. They are used for creating iterators for efficient loops, combinatoric iterators, infinite iterators,etc. They are useful when working with large datasets or streams of data where memory efficiency is important. We use next() function to get next value from the iterator. and list() function to convert the iterator to a list to see all the values at once.
#Examples:
import itertools
#Infinite iterators: count(start,step); cycle(p); repeat(element);
#count
counter = itertools.count(10,2)
print(f"Counter Iterator: {[next(counter) for _ in range(5)]}") # Output: [10, 12, 14, 16, 18]
#cycle
cycler = itertools.cycle(['A','B','C'])
print(f"Cycle Iterator: {[next(cycler) for _ in range(7)]}") # Output: ['A', 'B', 'C', 'A', 'B', 'C', 'A']
#repeat
repeater = itertools.repeat('Hello',3)
print(f"Repeat Iterator: {[next(repeater) for _ in range(3)]}") # Output: ['Hello', 'Hello', 'Hello']
#Combinatoric iterators: product(p1,p2,...,repeat=n); permutations(p,r); combinations(p,r); combinations_with_replacement(p,r);
#product
prod = itertools.product([1,2],['A','B'])
print(f"Product Iterator: {list(prod)}") # Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
#permutations
perm = itertools.permutations([1,2,3],2)
print(f"Permutations Iterator: {list(perm)}") # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
#combinations
comb = itertools.combinations([1,2,3],2)
print(f"Combinations Iterator: {list(comb)}") # Output: [(1, 2), (1, 3), (2, 3)]
#combinations with replacement
comb_wr = itertools.combinations_with_replacement([1,2,3],2)
print(f"Combinations with Replacement Iterator: {list(comb_wr)}") # Output: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
#Note: Itertools module is a powerful tool for creating iterators for efficient looping. Infinite iterators can generate an unending sequence of values, while combinatoric iterators help in generating permutations, combinations, and Cartesian products of input iterables. These iterators are memory efficient and can handle large datasets effectively.