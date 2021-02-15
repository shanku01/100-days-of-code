# DAY 8 OF 100 DAYS OF CODE
#Lambda
"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""

a = lambda x: x+15
print(a(9),"\n")

#Multiple argument
b= lambda x,y:x*y
print(b(4,5),"\n")

"""
The power of lambda is better shown
when you use them as an anonymous function inside another function.
"""

def myFunc(x):
    return lambda y:y*x
print(myFunc(4)(3),"\n")
myDoubler=myFunc(2)
print(myDoubler(4),"\n")
# you can you myFunc to create other multipler

myFourler = myFunc(4)
print(myFourler(5),"\n")

"""
NOTE - Use lambda functions
when an anonymous function is required for a short period of time.
"""


#Arrays
"""
Python does not have built-in support for Arrays,
but Python Lists can be used instead.
"""


#Classes and Objects
"""
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""

class MyClass:
    x= 5
obj1 = MyClass() #calling class and intializing object
print(obj1.x,"\n") #using object property


#_init() Function
"""
All classes have a function called __init__(),
which is always executed when the class is being initiated.
"""
class Person:
    def __init__(self,name,age): #using __init__() as constructor
        self.name = name
        self.age = age
p1 = Person("shasha",24)
print(p1.name,p1.age,"\n")


#Object Methods
"""
Objects can also contain methods.
Methods in objects are functions that belong to the object.
"""
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        return("bho bho")
d1 = Dog("Sera",5)
print(d1.name,d1.age,d1.bark(),"\n")

#Self parameter
"""
The self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like,
but it has to be the first parameter of any function in the class
"""

#Modify Object Proerties
d1.age = 3
print(d1.age,"\n")


#Delete Object and Object Properties
del p1.name

del p1

#Pass Statment to create empty class
class Me:
    pass


