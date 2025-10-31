#Blueprint for creating multiple objects with similar attributes and methods is a class in Python.
# A class serves as a template for creating objects (instances) that share common properties and behaviors.
# It encapsulates data for the object and methods to manipulate that data.
# Classes promote code reusability and organization by allowing developers to define a structure once and create multiple instances based on that structure.
# __init__ is a constructor. _proc_ is a protected method. __proc__ is a dunder method.
#examples:
#basic class
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def bark(self):
    print(f"{self.name} says Woof!")

#creating an instance
my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says Woof!

#classes with inheritance
class Student:
  def __init__(self,name,age,student_id, score):
    self.name = name
    self.age = age
    self.student_id = student_id
    self.score = score
  def study(self):
    print(f"{self.name} is studying.")

class GraduateStudent(Student):
  def __init__(self, name, age, student_id, score, thesis_topic):
    super().__init__(name, age, student_id, score)
    self.thesis_topic = thesis_topic
  def research(self):
    print(f"{self.name} is researching {self.thesis_topic}.")
#creating an instance of GraduateStudent
grad_student = GraduateStudent("Alice", 24, "GS123", 95, "Machine Learning")
grad_student.study()    # Output: Alice is studying.
grad_student.research() # Output: Alice is researching Machine Learning.
if(grad_student.score > 90):
    print(f"{grad_student.name} has a high score of {grad_student.score}.")

