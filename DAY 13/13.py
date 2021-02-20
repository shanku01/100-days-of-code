#DAY 13 OF 100 DAYS OF CODE

#DATA STRUCTURE
"""
Data structures are fundamental concepts of computer science which
helps is writing efficient programs in any language.

Python Specific Data Structures
These data structures are specific to python language
and they give greater flexibility in storing different types
of data and faster processing in python environment.

List: It is similar to array with the exception that the data
elements can be of different data types.
You can have both numeric and string data in a python list.

Tuple: Tuples are similar to lists but they are immutable which means
the values in a tuple cannot be modified they can only be read.

Dictionary: The dictionary contains Key-value pairs as its data elements.


The various data structures in computer science are divided broadly
into two categories shown below.
We will discuss about each of the below data
structures in detail in subsequent chapters.

Liner Data Structures

These are the data structures which store the data elements in a sequential manner.

Array: It is a sequential arrangement of data elements paired with the index of the
data element.

Linked List: Each data element contains a link to another element along
with the data present in it.

Stack: It is a data structure which follows only to specific order of operation.
LIFO(last in First Out) or FILO(First in Last Out).

Queue: It is similar to Stack but the order of operation is
only FIFO(First In First Out).

Matrix: It is two dimensional data structure in which the data element
is referred by a pair of indices.


Non-Liner Data Structures

These are the data structures in which there is no sequential linking of data elements.
Any pair or group of data elements can be linked to each other and
can be accessed without a strict sequence.

Binary Tree: It is a data structure where each data element
can be connected to maximum two other data elements and it starts with a root node.

Heap: It is a special case of Tree data structure where the data in the parent node
is either strictly greater than/ equal to the child nodes or
strictly less than it’s child nodes.

Hash Table: It is a data structure which is made of arrays associated with each other
using a hash function. It retrieves values using keys rather
than index from a data element.

Graph: .It is an arrangement of vertices and nodes where some of the
nodes are connected to each other through links.
"""

#2d array
"""
Two dimensional array is an array within an array. It is an array of arrays.
In this type of array the position of an data element is referred by
two indices instead of one.
So it represents a table with rows an dcolumns of data.
"""

twoDArray =[[2,3,1],[4,6,5],[9,7,8]] #intializing

print(twoDArray[0][1],"\n") #accesing one element

print(twoDArray[1],"\n") #accesing one row

for x in twoDArray: #looping through 2d array
    for y in x:
        print(y,end=" ")
    print()
print(" ")

twoDArray.insert(3,[3,6,1])

for x in twoDArray:
    for y in x:
        print(y,end=" ")
    print()
print(" ")

twoDArray[1][2] = 10 #updating 2d array

for x in twoDArray:
    for y in x:
        print(y,end=" ")
    print()
print(" ")

del twoDArray[1] #deleting row 

for x in twoDArray:
    for y in x:
        print(y,end=" ")
    print()
print(" ")



#Matrix
"""
Matrix is a special case of two dimensional array
where each data element is of strictly same size
"""


#Maps
"""
Python Maps also called ChainMap is
a type of data structure to manage multiple dictionaries together as one unit.
"""
import collections as col
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = col.ChainMap(dict1,dict2) # Creating a single dictionary
print(res.maps,"\n")

# Print all the elements from the result
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))

"""
When the element of the dictionary is updated,
the result is instantly updated in the result of the ChainMap.
"""

dict2['day4'] = 'Fri'
print(res.maps,'\n')



#Linked List

"""
A linked list is a sequence of data elements, which are connected together via links.
Each data element contains a connection to another data element in form of a pointer.
"""

#Creation of Linked List
"""
A linked list is created by using the node class.
We create a Node object and create another class to use this node object.
We pass the appropriate values thorugh the node object to point
the to the next data elements
"""

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init(self):
        self.head = None

    #Traversing a Linked List
    """
    Singly linked lists can be traversed in only forwrad direction starting form the first
    data element.We simply print the value of the next data element by assgining the
    pointer of the next node to the current data element.
    """    
    def printList(self):
        value = self.head
        while value is not None:
            print(value.data)
            value = value.next
        print("")


    #Insertion
    """
    Inserting element in the linked list involves reassigning the pointers from
    the existing nodes to the newly inserted node.
    """
    
    #Insertion at Beginning
    """
    This involves pointing the next pointer of the new data node to the current
   head of the linked list. So the current head of the linked list
   becomes the second data element and the new node becomes the head of the linked list.
   """
    def atBegining(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
    
    #Insertion at Last
    """
    This involves pointing the next pointer of the the current last node of the
    linked list to the new data node.
    """
    def atLast(self,newData):
        newNode= Node(newData)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while(lastNode.next):
            lastNode=lastNode.next
        lastNode.next = newNode

    #Insertion in between
    """
    This involves chaging the pointer of a specific node to point to the new node.
    That is possible by passing in both the new node and the existing node after which
    the new node will be inserted.
    """       
    def inBetween(self,givenNode,newData):
        if givenNode is None:
            print("The given node is absent")
            return
        newNode = Node(newData)
        newNode.next = givenNode.next
        givenNode.next = newNode

    #Removing Node
    """
    We can remove an existing node using the key for that node.
    """  
    def removeNode(self,key):
        head= self.head
        
        #checking if head got data
        if (head is not None):
            if(head.data == key):
                self.head = head.next
                head = None
                return
            
        #searching for node that has key
        while (head is not None):
            if head.data == key:
                break
            prev = head
            head = head.next
            
        if(head== None):
            print("key not found")
            return
        
        #if found the key from search
        prev.next = head.next
        head = None
        
list1 = LinkedList()
list1.head = Node("Mon")
n2 = Node("Tue")
n3 = Node("Wed")

list1.head.next = n2

n2.next =n3

list1.printList()

list1.atBegining("Sun")
list1.printList()

list1.atLast("Thu")
list1.printList()

list1.inBetween(list1.head.next,"Fri")
list1.printList()


list1.removeNode("Mon")
list1.printList()




