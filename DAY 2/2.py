#Day 2, 100 days of code
"""
Data Type
text str
number int flaot complex
sequence list tuple range
map dict
set set frozenset
boolean bool
binary bytes bytearray memoryview
"""
#specifying data
a =int(5)
b= str("asb")
c = float(6.4)
d = complex(1j)
e = list(("abc","bcd"))
f = tuple(("abc","bcd"))
g = range(7)
h = dict(name="abc",age=36) #key-value pair
i = set(("abc","bcd"))
j = frozenset(("abc","bcd"))
k = bool(5)
l = bytes(5)
m = bytearray(5)
n = memoryview(l)
print(a,b,c,d,e,f,g,h,i,j,k,l,m,n)

a = 1
print(type(a))
a= 13412423
print(type(a))
a= -12312
print(type(a))

a= 1.232
print(type(a))

a= 3+6j
print(type(a))

#changing type note complex number can't change into interget

#generating random number
import random
a=random.randrange(1,10)
print(a)

#sting and function
a="hello" #single line string
print(type(a))

a= """this is
a
multiline
sting
"""
print(a)

print(a[1])#string in pyhton are array

#looping in string
for x in a:
    print(x)
    
print(len(a)) #len function to measure length

print("this" in a)# gives true or false

print("this" not in a)# gives true or false

print(a[2:8]) #this is called slicing

print(a[:8]) #slice from start to 8

print(a[8:]) #slice from 8 to end
print(a) #slice doesn't change the original array/string

print(a[2:-5]) #using - index to get count from last

print(a.upper()) #to UPPERCASE
print(a) #doesn't alter orignal
print(a.lower()) #to lowercase

print(a.strip()) #removes white space

print(a.replace("h","a")) #replace
print(a)

print(a.split(" ")) #split using space

a= "hello"
b= "world"
print(a+b) #concatenate using +

#note concatenation happen in same type of data

number = 1
#to add number with sting we use format
print("hello {} world ".format(number)) #{} is used to format
print("hello {} world {}".format(4,5))
#index can be used to format
print("hello {1} world {0}".format(4,5))

print("i am \"good\"") #\ is used insert ""
print("i \\ am \"good\"") #\ is used insert \
print("i \n am \"good\"") #\n for new line
print("i \tam \"good\"") #\t is used for tab
print("\110\145\154\154\157") #\ for octal
print("\x48\x65\x6c\x6c\x6f") #\c for hex
