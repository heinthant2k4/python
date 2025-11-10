#Context Mangement in Python is typically handled using the 'with' statement along with context manager objects that define __enter__ and __exit__ methods. This allows for setup and teardown actions to be automatically managed, ensuring that resources are properly acquired and released, even in the presence of errors. Imagine we try to read a very huge file, using context manager ensures that the file is properly closed after its suite finishes, even if an exception is raised at some point.
#Example of using context manager with 'with' statement
class FileManager:
  def __init__(self,filename,mode):
    self.filename = filename
    self.mode = mode
    self.file = None
  def __enter__(self):
    self.file = open(self.filename,self.mode)
    return self.file
  def __exit__(self,exc_type, exc_value, traceback):
    if self.file:
      self.file.close()
#We just created a file manager context manager class that opens a file and ensures it is closed after use. Same can be done using built-in context managers.
#Using the FileManager context manager
with FileManager("some_text.txt","w") as f:
  f.write("Hello, World!")
# The file is automatically closed after the with block
#Example of using built-in context manager
with open("some_text.txt","w") as g:
  g.write("Hello again, World!")
# The file is automatically closed after the with block
#Output:
# The file "some_text.txt" will contain "Hello again, World!" as the last write operation overwrites the previous content.
#---------------------------------------------------------------