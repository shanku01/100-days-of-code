#Day 21 of 100 days of code

#Circular LinkedList

"""
Circular linked list is a linked list where all nodes are connected to form
a circle. There is no NULL at the end. A circular linked list can be a singly
circular linked list or doubly circular linked list.
"""

"""
Advantages of Circular Linked Lists:
1) Any node can be a starting point. We can traverse the whole list by
starting from any point. We just need to stop when the first visited node is
visited again.

2) Useful for implementation of queue. Unlike this implementation,
we don’t need to maintain two pointers for front and rear if we use
circular linked list. We can maintain a pointer to the last inserted node
and front can always be obtained as next of last.

3) Circular lists are useful in applications to repeatedly go around the list.
For example, when multiple applications are running on a PC, it is common for
the operating system to put the running applications on a list and then to
cycle through them, giving each of them a slice of time to execute, and then
making them wait while the CPU is given to another application.
It is convenient for the operating system to use a circular list so that
when it reaches the end of the list it can cycle around to the front ofthe list.

4) Circular Doubly Linked Lists are used for implementation of advanced
data structures like Fibonacci Heap.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circularLinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data)
        temp = self.head

        node.next= self.head

        #we need to change the last node next and head
        if self.head is not None: 
            while(temp.next != self.head):
                temp = temp.next
            temp.next = node

        else:
            node.next = node

        self.head = node

    def printList(self):
        temp = self.head

        if self.head is not None:
            while(1):
                print(temp.data)
                temp = temp.next

                #circular that's why we have to check for head
                if(temp ==self.head):
                    break
            print()


##Spliting List in Two haves
"""
1) Store the mid and last pointers of the circular linked list
using tortoise and hare algorithm.
2) Make the second half circular.
3) Make the first half circular.
4) Set head (or start) pointers of the two linked lists.
"""
def splitList(cList,cList1,cList2):
    slowP = cList.head
    fastP = cList.head

    #Base cases
    if slowP is None:
        print("Can not process empty List.")
        return
    
    #Checking if there are only 2 node
    if cList.head.next == cList.head:
        print("There are only two nodes.")
        return 

    while(fastP.next != cList.head and fastP.next.next != cList.head):
        fastP=fastP.next.next
        slowP = slowP.next

    #Finding the last node
    if(fastP.next.next == cList.head):
        fastP = fastP.next   

    #Creating list 2
    cList2.head = slowP.next
    fastP.next = cList2.head

    #Creating list1
    cList1.head = cList.head
    slowP.next = cList.head

#Testing
cList = circularLinkedList()
cList1 = circularLinkedList()
cList2 = circularLinkedList()
cList.push(1)
cList.push(2)
cList.push(3)
cList.push(4)
cList.printList()

splitList(cList,cList1,cList2)

cList1.printList()
cList2.printList()


        

