# DAY 5 OF 100 DAYS OF CODE

#Tuples

myTuple = ("apple","banana","cherry")
print(myTuple)
print(" ")

"""
Tuple items are ordered, unchangeable, and allow duplicate values.
"""
myTuple = ("apple","cherry","banana","cherry")
print(myTuple)
print(" ")

# myTuple[0]="abc" is invalid "unchangeable"

print(len(myTuple)) #classic len() function
print(" ")

myTuple =("abc",) #defining tuple with one value
print(type(myTuple))
print(" ")

myTuple =(1,4,5,7,True,"abc") #tuple can have anything as item
print(myTuple)
print(" ")

myTuple = tuple((1,2,3,4))#using tuple() to define tuple
print(myTuple)
print(" ")


#Accessing Tuple
print(myTuple[1]) #using index
print("")
print(myTuple[-1]) #using negative index
print(" ")
print(myTuple[1:3]) #using range 
print(" ")
print(5 in myTuple) #checking using in keyword 
print(" ")


#Updating Tuple
"""
You can not update tuple as they are unmutable,
you have to change them in other data type first
"""

#Updating using list
newList= list(myTuple)
newList[1]= 5 #updating item
newList.append(7) #extending tuple
newList.remove(1) #removing item
myTuple= tuple(newList)
print(myTuple)
print(" ")

del myTuple #deleting tuple


#Unpacking list
fruits = ("apple","banana","cherry")
(green,yellow,red)= fruits
print(green,yellow,red,"\n")

"""
If the number of variables is less than the number of values,
you can add an * to the variable name and the values will
be assigned to the variable as a list
"""
fruits = ("apple","banana","cherry","mango")
(green,*yellow,red)= fruits
print(green,yellow,red,"\n")


#Loop through a tuple
for x in fruits: #using in and for loop
    print(x)
print(" ")

for i in range(len(fruits)): #using index and range
    print(fruits[i])
print("")

i = 0
while i< len(fruits): #using index and while loop
    print(fruits[i])
    i+=1
print(" ")


#Joining Tupels
newFruits = ("orange","kiwi")
myFruits= fruits+newFruits #using + operator
print(myFruits,"\n")


#Multiple Tuple
print(fruits*2,"\n") #using * opearator


print(fruits.count("apple"),"\n") #finding count of item in tuple
print(fruits.index("mango"),"\n") #finding index of item

#SET

mySet={"apple","banana","cherry"}
print(mySet,"\n")
"""
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List,
 Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is both unordered and unindexed.
Sets are written with curly brackets.
"""

print(len(mySet),"\n") #Classic len() function

#Set can contain anything and can be declared using set function
newSet=set((1,"abc",True,5))
print(newSet,"\n")


#Accessing Set
for x in newSet: #index can't be used so in and for loop
    print(x)
print(" ")

print(False in newSet,"\n") #using in keyword to check item

#Once a set is created, you cannot change its items, but you can add new items.


#Adding item in set
newSet.add(9) #using add() to add data
print(newSet,"\n")

newSet.update(mySet) #using update() to set in existing set
print(newSet,"\n")

newSet.update(fruits) #update() can accept any itrable
print(newSet,"\n")


#Removing item from set
newSet.remove(9) #using remove() to remove item
print(newSet,"\n")

newSet.discard(9) #using discard() to remove item
#If the item to remove does not exist, discard() will NOT raise an error.
print(newSet,"\n")

newSet.pop() #using pop() to remove item
#but you never know which item will be removed as set is unorderd
print(newSet,"\n")

newSet.clear() #using clear() to empty set
print(newSet,"\n")

del newSet #deleting set


#Joining set
set1 = {1,2,4}
set2={"a","b"}
set3=set1.union(set2) #union to join to set
print(set3,"\n")

set1.update(set2) #using update() to set in existing set
print(set1,"\n")

"""
The intersection_update() method will keep only the items that are present in both sets.
"""
a={1,2,3}
b={2,3,4}
a.intersection_update(b)
print(a,"\n")

c=a.intersection(b) #To get the common without altering first set
print(c,"\n")

"""
The symmetric_difference_update() method will keep
only the elements that are NOT present in both sets.
"""
a={1,2,3}
b={2,3,4}
a.symmetric_difference_update(b)
print(a,"\n")

"""
The symmetric_difference() method will return a new set,
that contains only the elements that are NOT present in both sets.
"""
a={1,2,3}
b={2,3,4}
c=a.symmetric_difference(b)
print(c,"\n")



