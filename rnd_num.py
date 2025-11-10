#Random Number in Python is a module that provides various functions to generate random numbers.
import random
# Generate a random integer between 1 and 10
rand_int = random.randint(1,10)
print(f"Random Integer between 1 and 10: {rand_int}")
# Generate a random float between 0 and 1
rand_float = random.random()
print(f"Random Float between 0 and 1: {rand_float}")
# Generate a random choice from a list
choices = ['apple', 'banana', 'cherry', 'date']
rand_choice = random.choice(choices)
print(f"Random choice from list: {rand_choice}")
# Shuffle a list randomly
random.shuffle(choices)
print(f"Shuffled list: {choices}")
# Output:
# Random Integer between 1 and 10: 7
# Random Float between 0 and 1: 0.6394267984578837
# Random choice from list: cherry
# Shuffled list: ['date', 'banana', 'cherry', 'apple']
#---------------------------------------------------------------
#Note: The random module is widely used in simulations, games, and testing scenarios where randomness is required.