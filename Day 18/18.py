#Day 18 of 100 days of code

#LinkedList

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data)

        node.next = self.head
        self.head = node

    def printList(self):
        head = self.head

        while(head):
            print(head.data)
            head= head.next

        print()


def mergeList(head1,head2):
    head = None


    #base Casees
    if head1==None:
        return head2
    
    if head2==None:
        return head1

    #this will check the first node of each list and push to new list
    if head1.data<head2.data:
        head = head1
        head.next = mergeList(head1.next,head2)
    elif head1.data==head2.data:
        head =head1
        head.next = mergeList(head1.next,head2.next)
    else:
        head = head2
        head.next = mergeList(head1,head.next)
    
    return head

#mergining two list without any extra space
def merge(head1,head2):
    #base cases
    if head1==None:
        return head2
    if head2==None:
        return head1

    #cheking node data and merging lsit without using extra space
    if head1.data<head2.data:
        head1.next =merge(head1.next,head2)
        return head1
    elif head1.data == head2.data:
        head1.next =merge(head1.next,head2.next)
        return head1
    else:
        head2.next = merge(head1,head2.next)
        return head2


#Detecting Loop and removing it
"""
We know that Floyd’s Cycle detection algorithm terminates when fast
and slow pointers meet at a common point. We also know that
this common point is one of the loop nodes. Store the address of
this in a pointer variable say ptr2.After that start from the head of
the Linked List and check for nodes one by one if they are reachable from ptr2.
Whenever we find a node that is reachable,
we know that this node is the starting node of
the loop in Linked List and we can get the pointer to the previous of this node.
"""
def removeLoop(head,loopNode):

    #moving pointer till we find first node of loop
    ptr1 = head
    while(1):
        #moving pointer 2 to get the last node to loop
        ptr2 = loopNode
        while(ptr2.next != loopNode and ptr2.next !=ptr1):
            ptr2 =ptr2.next

        if ptr2.next ==ptr1:
            break
        ptr1 =ptr1.next

    ptr2.next =None
    
def detectAndRemoveLoop(head):
    slowP = fastP = head

    #looping till we find looNode
    while(slowP and fastP and fastP.next):
        slowP = slowP.next
        fastP = fastP.next.next

        if slowP ==fastP:
            removeLoop(head,slowP)
            return "Loop found and sorted"
    return "No Loop Found"


#Creating List for test
list1= LinkedList()
list1.push(6)
list1.push(4)
list1.push(2)
list1.push(1)
list1.printList()

list2= LinkedList()
list2.push(7)
list2.push(5)
list2.push(4)
list2.push(2)
list2.printList()

list3 = LinkedList()
list3.head = mergeList(list1.head,list2.head)
list3.printList()

list4 = LinkedList()
list4.head = merge(list1.head,list2.head)
list4.printList()

#creating a looped list
list1.head.next.next.next = list1.head.next

print(detectAndRemoveLoop(list2.head))

print(detectAndRemoveLoop(list1.head))

detectAndRemoveLoop(list1.head)

list1.printList()
