#DAY 4 OF 100 DAYS OF CODE

#LIST

myList = ["apple","banana","cherry"]
print(myList)
print(" ")

#can also be declared using list()
listA= list(("apple","cherry"))
print(listA)
print(" ")

"""
you can not go out of any index but you can use append to insert new element
list are mutable thats mean can be changed
list can have repeating values 
"""
myList.append("apple")
print(myList)
print(" ")

print(len(myList)) #classic len() function
print(" ")

listA=[1,2,3,4,5] #can have int, string , boolean ,objects
print(listA)
print(" ")

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.
"""


#Accessing List
print(myList[0]) #accessing using index
print(" ")
print(myList[-1]) #using - index to get from last
print(" ")
print(myList[2:5]) #using range to access items
print(" ")

print(1 in myList) #using in to check item
print(" ")


#Updating List
myList[1]="pea" #using index
print(myList)

myList[1:3]=["pea","banana"] #using range
print(myList)
print(" ")


#Insering item in list
myList.insert(2,"watermelon") #inserting on specific index
print(myList)
print(" ")

myList.append("orange") #inserting at tail
print(myList)
print(" ")

myList.extend(["mango","pineapple","papaya"]) #extending list using other list
print(myList)
print(" ")

#extend can add tuple,list, dict any iterable object
myList.extend(("mango","pineapple","papaya"))
print(myList)
print(" ")

#Removing elements
myList.remove("mango") #will remove the first mango
print(myList)
print(" ")

myList.pop(0) #removing element using index
print(myList)
print(" ")

myList.pop() #removing last element
print(myList)
print(" ")

del myList[0] #removing using del keyword
print(myList)
print(" ")

del myList #removes list

myList =["apple","mango","cherry"]
print(myList)
print(" ")

myList.clear() #clears function clear the list
print(myList)
print(" ")

#Looping through a List

myList =["apple","mango","cherry"]

for x in myList: #loop through item
    print(x)
print(" ")

for x in range(len(myList)): #loop through index
    print(myList[x])
print(" ")

#loop using while don't forget to define variable first
i=0
while i < len(myList): 
    print(myList[i])
    i+=1
print(" ")

[print(x) for x in myList] #looping using List Comprehension
print(" ")

    
#List Coprehension "newlist = [expression for item in iterable if condition == True]"
newList = [x for x in myList if "a" in x]
print(newList)
print(" ")


#Sorting list
myList.sort() #sort list and sorting is case sensitive
print(myList)
print(" ")

myList.sort(reverse = True) #sort list in decending order
print(myList)
print(" ")

#using function
def myfunc(n):
  return abs(n - 50) #abstaract function

newList = [100, 50, 65, 82, 23]
newList.sort(key = myfunc) #you can pass any function here
print(newList)
print(" ")

myList = ["banana", "Orange", "Kiwi", "cherry"]
myList.sort(key = str.lower) #case insenstive sorting
print(myList)
print(" ")

myList.reverse() #reversing string
print(myList) 
print(" ")


#Coping List
newList =myList.copy() #using copy function
print(newList)
print(" ")

newList1 =list(newList) #using list function
print(newList1)
print(" ")


#Joing List
myList = newList + newList1 #using + operator
print(myList)
print(" ")

newList.extend(newList1) #using extend function
print(newList)
print(" ")

for x in myList:
    newList.append(x) #using append with loop
print(newList)
print(" ")



