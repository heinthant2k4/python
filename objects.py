#Objects are instances of classes which encapsulate data and functionality together.
#Everything in Python is an object including numbers, strings, functions, and even classes.
#Objects have attributes (data) and methods (functions) that operate on the data.
#You can create your own custom objects by defining classes using the class keyword.
#Example of defining a simple class and creating an object
class Dog:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def bark(self):
    return f"{self.name} says Woof!"

my_dog = Dog("MelLone", 3)
print(my_dog.bark())  # Output: MelLone says Woof!
#In this example, we defined a Dog class with attributes name and age, and a method bark().
#We then created an instance of the Dog class called my_dog and called its bark() method.
#You can create multiple instances of the same class with different data.
#-----------------------------------------------------------------------------------------
#Inheritance
class Animal:
  def __init__(self, species):
    self.species = species

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__("Cat")  # Call the parent class's __init__ with the correct argument
        self.name = name
        self.age = age

my_cat = Cat("ShweWar", 2)
print(f"My cat's name is {my_cat.name}, age is {my_cat.age}, and species is {my_cat.species}.")
#In this example, Cat class inherits from Animal class, gaining its attributes and methods.
#This allows for code reuse and creating hierarchical relationships between classes.
#-----------------------------------------------------------------------------------------
#Properties of a class(protected, private and public)
class Person:
  def __init__(self,name,age):
    self.name = name          # public attribute
    self._age = age          # protected attribute[_ indicates protected]{Protected attributes should not be accessed directly outside the class or its subclasses}
    self.__ssn = "123-45-6789"  # private attribute[__ indicates private]{Private attributes cannot be accessed directly outside the class}
  def get_ssn(self):          # public method to access private attribute
    return self.__ssn

person_1 = Person("Hein", 21)
print(person_1.name)
print(person_1._age)
print(person_1.get_ssn())
#Note: Python is shit when it comes to privacy of attributes in classes but it is still a good practice to write _ or __ to indicate the level of accesibility of an attribute.
#-----------------------------------------------------------------------------------------
#Encapsulation is a very important concept in Python which allows you to bundle attrs and methods that operate on a single entity to a class.
class Car:
  def __init__(self,make,model):
    self._make = make
    self._model = model
  def display_info(self):
    return f"Make: {self._make}\n Model: {self._model}"
  
  @property
  def model(self):
    return self._model
  
  @model.setter
  def model(self,model):
    self._model = model

car = Car("Toyota", "Corolla")
print(car.display_info())

car.model = "Altis"
print(car.model)

