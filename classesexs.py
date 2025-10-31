
"""Practice Exercises:

Create a Book class with title, author, pages, and a method to check if it's a "long book" (>300 pages)
Create a Temperature class that stores Celsius and has methods to convert to Fahrenheit and Kelvin
Create a Playlist class that can add/remove songs, shuffle, and get total duration"""
#book class
class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
  def is_long_book(self):
    if(self.pages > 300):
      print(f'"{self.title}" by {self.author} is a long book.')
    else:
      print(f'"{self.title}" by {self.author} is not a long book.')
#creating an instance of Book
book1 = Book("War and Peace", "Leo Tolstoy", 1225)
book2 = Book("Little Prince", "Antoine de Saint-Exupéry", 96)
book1.is_long_book()  # Output: "War and Peace" by Leo Tolstoy is a long book.
book2.is_long_book()  # Output: "Little Prince" by Antoine de Saint-Exupéry is not a long book.

#temperature class
class Temperature:
  def __init__(self, celsius):
    self.celcius = celsius
  def to_fahrenheit(self):
    fahrenheit = (self.celcius * 9/5) + 32
    return fahrenheit

today_temp = Temperature(25)
print(f"Temperature in Fahrenheit: {today_temp.to_fahrenheit()}°F")  #Output: Temperature in Fahrenheit: 77.0°F

#playlist class
import random
class Playlist:
  def __init__(self):
    self.songs = []
  def add_song(self,song,duration):
    self.songs.append((song,duration))
  def remove_song(self,song):
    self.songs = [s for s in self.songs if s[0] != song]
  def shuffle(self):
    random.shuffle(self.songs)
  def total_duration(self):
    total = sum(duration for song, duration in self.songs)
    return total
  
#creating an instance of Playlist
my_playlist = Playlist()
my_playlist.add_song("Song A", 210)
my_playlist.add_song("Song B", 180)
my_playlist.add_song("Song C", 240)
print(f"Total duration: {my_playlist.total_duration()} seconds")  # Output: Total
# duration: 630 seconds
my_playlist.shuffle()
print("Shuffled Playlist:")
for song, duration in my_playlist.songs:
  print(f"{song} - {duration} seconds")
my_playlist.remove_song("Song B")
print("Playlist after removing Song B:")
for song, duration in my_playlist.songs:
  print(f"{song} - {duration} seconds")
# Output will vary due to shuffling: