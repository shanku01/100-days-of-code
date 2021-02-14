#DAY 7 OF 100 DAYS OF CODE

#Statements

if 4>5:
    print("5 is greater than 6")
elif 1>5: #when if is false
    print("7 is greater than 5")
else: #when everything is false
    print("printing else\n")


#Short hand statements

if 5>3: print("5 is greater than 3\n")

print("5 is greater than 3\n") if 1>3 else print("3 is greater \n") 


#Multiple if else

a= 300
b= 300
print("A") if a>b else print ("=") if a==b else print("B")


#Using and-or
c= 400
if a>=b and c>a:
    print("c is biggest\n") #if both are true

if a>=b or a>c:
    print(a,"\n") #if one of the condition is true


#Nested if
if a>=b:
    if a>c:
        print("A is biggest \n")
    else:
        print("C is biggest \n")

if c>a:
    pass #using pass keyword to pass the condition


#Loops

#While Loop
i =0
while i>5:
    i+=1
    if i==2:
        continue #skip a specific condition
    if i==3:
        break #breaking after a specific condition
    print(i) #while condition is true
else: #if loops complete
    print("I is not samller than 5 ",i) 
print("")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6\n")


#For Loop
"""
A for loop is used for iterating over a sequence (that is either a list,
a tuple, a dictionary, a set, or a string).
"""

fruits=["apple","banana"]
for x in fruits:
    print(x)
    if x=="banana":
        break #to break the loop
    for y in x: #for in string
        print(y)
    print("")
print("\n")

for x in fruits:
    print(x)
    if x=="apple":
        continue #to skip the loop
    for y in x: #nested for loop
        print(y) #for loop in string
    print("")
print("\n")

for x in range(2, 30, 3):
  print(x) #print range 2 to 30 with 3 increment
else:
    print("Range Finished\n")


#Funtions
def myFunction():
    print("myFunction is running \n")
myFunction() #calling function

def myFunction1(arg="bcd"): #default parameter
    print(arg,",Passing argumnet \n")
myFunction1("abc") #calling function
"""
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

def myFunction2(name,lName):
    print(name+" "+lName,",Passing multiple argumnets \n")
myFunction2("abc","bcd") #calling function


#Multiple argumnet using one variable
def myFunction3(*arg):
    print(type(arg),"\n")
    for x in arg:
        print(x)
    print("Passing multiple arguments using one parameter\n")
myFunction3("abc","bcd") #calling function


#Keyword Arguments
def myFunction4(b,a):
    print(a,"Passing multiple arguments using keys\n")
myFunction4(a="abc",b="bcd") #calling function

def myFunction5(**kwarg):
    print(type(kwarg),"\n")
    print(kwarg["b"],"Passing multiple arguments using key and one parameter\n")
myFunction5(a="abc",b="bcd") #calling function

def myFunction6(food):
    print(type(food),"\n") #paramter as list
    for x in food:
        print(x)
fruits = ["apple", "banana"]
myFunction6(fruits)
print("")

def func(x):
    return x+1 #using return to process parameter
print(func(3),"\n")

def newFunction():
    pass #using pass do nothing


#Recursion
"""
Recursion is a common mathematical and programming concept.
It means that a function calls itself.
This has the benefit of meaning that you can loop through data to reach a result.
"""
def newFunction1(x):
    if x > 6:
        result = x+newFunction1(x-1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example\n")
newFunction1(12)
print("\n")




