## Day 34 of 100 days of Code

# Circular Linked List

class Node:
    def __init__(self,data=None,next=None,prev =None):
        self.data = data
        self.next = next
        self.prev = prev

def push(head,ndata):
    node = Node(data=ndata,next=head)

    if head is None:
        head = node
        head.next = node
        head.prev = node
        return head
    node.prev = head.prev
    head.prev.next = node
    head.prev = node
    head = node
    return head


def append(head,ndata):
    node = Node(data=ndata,next=head)

    if head is None:
        head = node
        head.next = node
        head.prev = node
        return head
    node.prev = head.prev
    head.prev.next = node
    head.prev = node
    return head

def insertAfter(head,val1,val2):
    #base case
    if head is None or val1 is None and val2 is None:
        return

    temp = head
    while(temp.data!= val2):
        temp= temp.next

    node=Node(data =val1,next=temp.next,prev=temp)

    temp.next.prev =node
    temp.next = node
    

def printList(head):
    temp = head
    
    if temp is None:
        return
    
    while(temp.next!=head):
        print(temp.data)
        temp= temp.next
    print(temp.data)
    print("")
        
#Testing
head = None

head = push(head,2)
head = push(head,3)
head = push(head,4)
head = push(head,5)
head = push(head,6)
printList(head)

head = append(head,2)
head = append(head,3)
head = append(head,4)
head = append(head,5)
head = append(head,6)
printList(head)

insertAfter(head,5,2)
printList(head)

#Advantages: 
"""
List can be traversed from both the directions i.e. from head to tail or from tail to head.
Jumping from head to tail or from tail to head is done in constant time O(1).
Circular Doubly Linked Lists are used for implementation of advanced data structures like Fibonacci Heap.
"""

#Disadvantages 
"""
It takes slightly extra memory in each node to accommodate previous pointer.
Lots of pointers involved while implementing or doing operations on a list. So, pointers should be handled carefully otherwise data of the list may get lost.
"""

#Applications of Circular doubly linked list 

"""
Managing songs playlist in media player applications.
Managing shopping cart in online shopping.
"""
