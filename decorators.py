# Decorator = a function that takes another function as an argument,
# adds some kind of functionality and returns another function.
def add_sprinkles(func):#for modifying functions with arguments
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):#for modifying functions without arguments
    def wrapper():
        print("*You add fudge 🍫*")
        func()
    return wrapper

@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")
get_ice_cream("vanilla")

@add_fudge
def make_sundae():
    print("Sundae is ready!")
make_sundae()