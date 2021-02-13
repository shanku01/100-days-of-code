#DAY 6 OF 100 DAYS OF CODE

#SET FUNCTION

newSet={1,2,3,4}
thisSet={3,4,5,6}

print(newSet.isdisjoint(thisSet),"\n") #returns true if there is sum intersection

print(newSet.issubset(thisSet),"\n") #returns true if found subset

print(newSet.issuperset(thisSet),"\n") #returns true if superset is found


#Dictionary
"""
A dictionary is a collection which is ordered*,
changeable and does not allow duplicates.
"""
thisDict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
    }
print(thisDict,"\n")

print(thisDict["brand"],"\n") #accessing item

print(len(thisDict),"\n") #classic len() function

thisDict={
    "brand":"Ford",
    "model":["Mustang","etc"],#Dictionary can have anything as item
    "year":1964
    }
print(thisDict,"/n")


#Accesing Dictionary

x = thisDict.get("model") #using get() to get value of key
print(x,"\n")

x= thisDict.keys()#return all the keys of dictionary
print(x,"\n")

thisDict["color"] = "Red" #adding new keys
print(x,"\n")

x=thisDict.values() #getting all the values
print(x,"\n")

x= thisDict.items() #returns each item as tuple
print(x,"\n")

print("model" in thisDict,"\n") #checking a key using in keyword


#Updating Dictionary
thisDict["year"]=2018 #using keys to change value
print(thisDict,"\n")

thisDict.update({"year":2019}) #using update function to update value
print(thisDict,"\n")


#Adding items
thisDict["type"]="SUV" #using key to add new item
print(thisDict,"\n")

thisDict.update({"Upcoming Model":2021}) #using update function to add items
print(thisDict,"\n")


#Removing items
thisDict.pop("model") #using pop to remove key-value
print(thisDict,"\n")

thisDict.popitem() #removes last inserted item
print(thisDict,"\n")

del thisDict["color"] #removing key-value using del keyword
print(thisDict,"\n")

thisDict.clear() #to clear dictoinary
print(thisDict,"\n")
del thisDict #to delete whole dictionary


#Loop through a Dictionary
thisDict={
    "brand":"Ford",
    "model":["Mustang","etc"],#Dictionary can have anything as item
    "year":1964
    }

for x in thisDict:
    print(x) #returns all the keys
print("")

for x in thisDict:
    print(thisDict[x]) #returns all the values
print("")

for x in thisDict.values(): #using values()
    print(x) #returns all the values
print("")

for x in thisDict.keys(): #using keys()
    print(x) #returns all the keys
print("")

for x,y in thisDict.items(): #using items()
    print(x,y) #returns all the key-value pairs
print("")


#Copying Dictionary
newDict= thisDict.copy() #using copy()
print(newDict,"\n")

myDict = dict(newDict) #using dict()
print(myDict,"\n")


#Nested Dictionary
user={
    "name":"Shasha",
    "age":20,
    "Father":{
        "name":"Pasha",
        "age":40
        }
    }
print(user,"\n")


#Dictionary Functions
x=("1","2","3")
y=("abc","bcd","def")
myDict = dict.fromkeys(x,y) #fromkeys() to create dictionary from tuples 
print(myDict,"\n")

#The setdefault() method returns the value of the item with the specified key.
x = thisDict.setdefault("color", "white")
print(x)

