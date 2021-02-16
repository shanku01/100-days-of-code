#DAY 9 OF 100 DAYS OF CODE

#Inheritance
"""
Inheritance allows us to define a class that inherits all the methods and properties
from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""

class Person: #Parent class
    def __init__(self,name,lName):
        self.name= name
        self.lName= lName
        
    def getPerson(self):
        print(self.name,self.lName,"\n")

class Student(Person): #Child class inheriting parent 
    pass
s1 = Student("shasha","Jenson")
s1.getPerson()

class Teacher(Person):
    def __init__(self,name,lName): #Child can have it's own properties
        self.name=name
        self.lName = lName

t1 = Teacher("Sha","Son")
t1.getPerson()

#super()
"""
By using the super() function, you do not have to use the name of the parent element,
it will automatically inherit the methods and properties from its parent.
"""

class Footballer(Person):
    def __init__(self,name,lName):
        super().__init__(name,lName)

    def goal(self): #child can have it's own method
        print("Fantasic Goal by ",self.name,"\n")
        
f1 = Footballer("Ronaldo","7")
f1.getPerson()
f1.goal()


#Iterators
"""
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that
you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__().

Lists, tuples, dictionaries, and sets are all iterable objects.
They are iterable containers which you can get an iterator from.
"""

myTuple = ("apple","banana","cherry")
myIter = iter(myTuple)

print(next(myIter),"\n")
print(next(myIter),"\n")
print(next(myIter),"\n")

"""
you can user any iterable to retun an iterator
"""

myStr = "apple"
myIter1= iter(myStr)

print(next(myIter1),"\n")
print(next(myIter1),"\n")
print(next(myIter1),"\n")


#Looping through an Iterator
for x in myStr:
    print(x)
print("")
"""
The for loop actually creates an iterator object
and executes the next() method for each loop.
"""


#Creating class as an Iterator
class MyNumbers:
    def __iter__(self):
        self.a =1
        return self

    def __next__(self):
        if self.a<=20:
            x= self.a
            self.a += 1
            return x
        else:
            raise StopIteration #using to stop the iteration

n1 = MyNumbers()
myIter2 = iter(n1)

for x in myIter2:
    print(x)
print("\n")


#Scope
"""
A variable is only available from inside the region it is created.
This is called scope.
"""

#Local Scope
"""
A variable created inside a function belongs to the local scope of that function,
and can only be used inside that function.
"""

def myFunc():
    c = 100
    return c
print(myFunc(),"\n")


#Global Scope
"""
A variable created in the main body of the Python code is a global variable
and belongs to the global scope.

Global variables are available from within any scope, global and local.
"""
x = 200
def myFunc1():
    return x

print(myFunc1(),"\n")

def myFunc2():
    global x #using global keyword to update global variable
    x=100
    return "Changed global"

print(myFunc2(),x,"\n")


#Module
"""
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
"""

#Creating Module
"""
To create a module just save the code you want in a file with the file extension .py
"""

import Module1 as m1 #importing module as m1

ans = m1.myFunc(4)(4) #using module function
print(ans,"\n")

"""
The module can contain functions, as already described,
but also variables of all types.
"""
person = m1.person1
print(person,"\n")

"""
You can choose to import only parts from a module, by using the from keyword.
"""

from Module1 import person1 as p1

print(p1,"\n")



