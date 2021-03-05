## Day 26 of 100 Days of Code

#Doubly Linked List

import gc #Garbage Collection

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def deleteNode(self,dNode):

        #base case
        if self.head == None or dNode is None:
            print("Only God can delete None!!")
            return

        #if dNode is head
        if self.head == dNode:
            self.head = dNode.next


        #dnode is in Middle
        if dNode.next is not None:
            dNode.next.prev = dNode.prev

        #changing prev if it's not None
        if dNode.prev is not None:
            dNode.prev.next = dNode.next

        gc.collect() #collecting the unlinked node


    #deleting at specific postion
    def deleteAtPostion(self,key):
        #base case
        if self.head == None or key <= 0:
            print("Only God can delete None!!")
            return

        temp = self.head #intializing temp for loop
        i =1

        #Looping till we find the postion 
        while(temp and i<key):
            temp = temp.next
            i+=1

        if temp is None:
            print("Sorry but I don't have that postion")
            return

        self.deleteNode(temp)

    def push(self,nData):


        #base case
        if self.head == None:
            self.head = Node(data=nData)
            return

        node = Node(data = nData,next= self.head)

        self.head.prev = node #setting prev

        self.head = node #making new head

    def traverse(self):

        #base case
        if self.head == None:
            print("Push some elements first!!")
            return
        
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next
        print()

#testing

dlist = DoublyLinkedList()

dlist.push(1)
dlist.push(2)
dlist.push(3)
dlist.push(1)

dlist.traverse()

dlist.deleteNode(dlist.head) #deleting head
dlist.traverse()


dlist.deleteNode(dlist.head.next) #deleting middle
dlist.traverse()

dlist.deleteNode(dlist.head) #deleting middle
dlist.traverse()

dlist.push(4)
dlist.push(2)
dlist.push(3)
dlist.traverse()

dlist.deleteAtPostion(2)
dlist.traverse()
        
            
        
