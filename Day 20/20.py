## Day 20 of Linked List

## Union and Intersection of two Linked List

"""
Initialize the result list as NULL.

Traverse list1 and look for its every element in list2,
if the element is present in list2, then add the element to result.
Union (list1, list2):

Initialize the result list as NULL. Traverse list1 and add all of
its elements to the result.

Traverse list2. If an element of list2 is already present in result
then do not insert it to result, otherwise insert.

This method assumes that there are no duplicates in the given lists.
"""


class Node:
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
        temp = self.head

        while(temp):
            print(temp.data)
            temp = temp.next
        print()

def getUnion(head1,head2):
    node = LinkedList()

    while(head1):
        node.push(head1.data)
        head1 = head1.next

    while(head2):
        if(isPresent(node.head,head2)):
            node.push(head2.data)
        head2 = head2.next

    return node.head

def isPresent(head1,head):
    temp = head1
    while(temp):
        if(temp.data==head.data):
            return False
        temp=temp.next
    return True

def getIntersection(head1,head2):
    node = LinkedList()
    while(head2):
        if(isPresent(head1,head2) == False):
            node.push(head2.data)
        head2 = head2.next

    return node.head

list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.printList()

list2 = LinkedList()
list2.push(1)
list2.push(4)
list2.push(5)
list1.printList()

result = LinkedList()
result.head = getUnion(list1.head,list2.head)
result.printList()

result1 = LinkedList()
result1.head = getIntersection(list1.head,list2.head)
result1.printList()
