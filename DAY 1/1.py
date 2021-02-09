# 100 days of code day 1

x=3;
if x==2:
    print(x);
print("pyhton is good")
#this is a comment
"""
this
is
a
multiline
comment
"""

# variable casting
x= str(3)
y="3"
y = int(y)

print(type(x))#type to check type of variable
y=5
z= int(x)
s=str(y)

#value of x will be same
print(type(x),y,z,s)

x=4
X=4

#case sensititve
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

#camelCase is general for variable and function

x=y=z= 2 #you can give one value to nummber of variable like this
print(x,y,z)

#packing and unpacking list
fruits = ["apple","blabal","banana","cherry"]
x,y,z,s=fruits
print(x,y,z)

#using + to combine characters
x = "Hey"
print(x+" i am here")

#+ for addition
y = 5
z=6
print(y+z+X)

#error if you combine diffrent variable

#Global Variable
x ="Hey"
def myFunc1():#defining function
    print(x+" i am here")
myFunc1()#calling function

#global keyword for global function

def myFunc():
    global x #using global to call global x
    x= "you"
myFunc()

print(x+" are here")




