## Day 25 of 100 days of code

#Doubly Linked List

"""
A Doubly Linked List (DLL) contains an extra pointer,
typically called previous pointer,
together with next pointer and data which are there in singly linked list.
"""

#Doubly Node
class Node:
    def __init__(self,next=None,prev=None,data=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    #inserting element in head
    def push(self,ndata):

        node =Node(data = ndata) #intializing node

        node.next = self.head
        node.prev = None

        if self.head != None:
            self.head.prev = node

        self.head = node

    #inserting after a given node
    def insertAfter(self,ndata,prevN):

        node = Node(data =ndata,prev=prevN)

        node.next = prevN.next

        prevN.next = node

        #making next's prev to node
        if node.next != None:
            node.next.prev = node
            
    #inserting after a given node
    def insertBefore(self,ndata,nextN):

        node = Node(data =ndata,next=nextN)

        node.prev = nextN.prev

        nextN.prev = node

        #making next's prev to node
        if node.prev != None:
            node.prev.next = node
        else:
            self.head = node
            
    #inserting at last
    def append(self,ndata):

        node = Node(data = ndata)

        last =self.head

        if self.head is None:
            node.prev = None
            self.head = node
            return

        while(last.next!= None):
            last = last.next

        last.next = node
        node.prev = last

    def traveseForward(self):
        temp = self.head
        while(temp):
            print(temp.data, end= " ")
            temp = temp.next
        print("")

    def traveseBackward(self):
        temp = self.head

        while(temp.next):
            temp = temp.next

        while(temp):
            print(temp.data, end=" ")
            temp = temp.prev
        print("")

#testing
dlist = DoublyLinkedList()

dlist.push(2)
dlist.push(3)
dlist.push(4)
dlist.traveseForward()

dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.append(5)
dlist.traveseBackward()

dlist.insertAfter(6,dlist.head.next)
dlist.insertAfter(7,dlist.head.next)
dlist.traveseForward()


dlist.insertBefore(10,dlist.head.next)
dlist.insertBefore(11,dlist.head.next)
dlist.traveseForward()

            
    
        
