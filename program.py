# #This will not be executed

# # print('hello!');

# # a = 'hello'
# # print(a) 

# # Data Types in Python
# # There are lots of different types of data that you can use in python

# # String (text)
# # Integers (whole numbers)
# # Float (decimal numbers)
# # Booleans (True/False)
# # You can convert one data type to another

# a = str(1) #a = "1"
# b = int("5") #b = 5
# c = float(4) #c = 4.0
# d = int(5.7) #d = 5
# # Performing Calculations
# a = 1
# b = a + 1 #b = 2
# c = b * 3 #c = 6
# d = c - 1 #d = 5
# e = d / 2 #e = 2.5
# f = d ** 2 #exponent: f = 25
# # String Operations
# a = "first string"
# b = "second string"
# c = a + " " + b
# # Lists
# # You can create lists of things

# a = [1, 5, "some string", True, 5.6]
# # You can even have lists of lists

# a = [
#     [1, 2, 3], #first row
#     [4, 5, 6], #second row
#     [7, 8, 9], #third row
#     [10] #fourth row
# ]
# # You can conceptualize a list of lists however you want

# # ACTIVITY
# # If you want to make the previous example have columns instead of rows, do you need to change anything?

# # Access an element of a list
# # Lists have elements stored at numerical indexes, starting at 0

# a = [1, 5, "some string", True, 5.6]
# print(a[0]) #1
# print(a[1]) #5
# print(a[4]) #5.6
# # Dictionaries
# # You can create JS style objects in python called dictionaries

# # Dictionaries use array access syntax:
# my_car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(my_car["brand"])
# # You can also have lists in dictionaries and dictionaries in lists!

# a = [
#     {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
#     },
#     [4, 5, 6],
#     [7, 8, 9],
#     [10]
# ]
# print(a)

# b = {
#   "firstGrade": ["Bobby", "Kyle", "Suzy"],
#   "secondGrade": ["Jennifer", "Jasmine", "Javier"],
#   "thirdGrade": "Nobody, they all failed last year!"
# }
# print(b)
# # Perform a set of commands depending on a situation
# a = 22
# if a < 10:
#     print("a is less than 10")
# elif a == 10:
#     print("a is 10")
# else:
#     print("a is greater than 10")

# # The conditions can be

# # < less than
# # > greater than
# # <= less than or equal to
# # >= greater than or equal to
# # == an exact match
# # # != not equal to
# # You can also compare strings:

# a = 'oh hai!'
# if a == 'oh hai!':
#     print('this works')
# # You can combine conditional statements:

# # check to see if both conditions are met:

# a = 1
# b = 2
# if a == 1 and b == 2:
#   print('y') # will print only when both a==1 AND b==2
# else:
#   print('n') # will print if either condition is false

# if a == 0 and b == 2:
#   print('y') # will print only when both a==1 AND b==2
# else:
#   print('n') # will print if either condition is false

# # check to see if either condition is met:

# a = 2
# b = 2
# if a == 1 or b == 2:
#   print('y') # will print when either a==1 OR b==2
# else:
#   print('n') # will print if both conditions are false

# if a == 1 or b == 1:
#   print('y') # will print when either a==1 OR b==2
# else:
#   print('n') # will print if both conditions are false



###### PART 2 

# user_input = input("please enter your name: ")
# print("Hello, " + user_input + "!")

# a= 10 
# while a < 20:
#   print("The value of a is currently: " + str(a) )
#   a += 1
#   print("end of loop") #notice the indent

# foods = ['hot dogs', ' beer', 'bald eagles']
# for food in foods:
#   print(food)

# def greet(name):
#   print('hi, ' + name)

# greet('nate') 

# def add(value1, value2):
#   return value1 + value2

# print(add(1,3))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name + ". My age is " + str(self.age)) 

  def work(self):
    print("Boring...")


class SuperHero(Person):
  def __init__(self, name, age, powers):
    super().__init__(name, age)
    self.powers = powers

  def greet(self):
    super().greet(
      self.listPowers()
    )  

  def listPowers(self):
    for power in self.powers:
      print(power)

  def work(self):
    print('to Action!')

me = Person('Nate', 30)
me.greet()
me.work()
# sally = Person('Sally', 53)
# sally.greet()
superman = SuperHero('Clark Kent', 200, ['flight', 'strength', 'invulnerability'])
superman.greet()
superman.listPowers()
superman.work()