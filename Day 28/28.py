## Day 28 of 100 days of code

#Doubly Linked List

#Creating Node data 
class Node:
    def __init__(self,data =None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

#Creating Doubly Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    #Function to merge two linked list
    def merge(self,first,second):

        #base cases
        if first is None:
            return second

        if second is None:
            return first

        #checking for bigger data and calling merge
        if first.data < second.data:
            
            first.next = self.merge(first.next,second)
            first.next.prev = first
            first.prev = None
            
            return first

        else:
            
            second.next = self.merge(first,second.next)
            second.next.prev = second
            second.prev = None

            return second

    #merge sort
    def mergeSort(self,tempHead):

        #base case
        if tempHead is None or tempHead.next is None:
            return tempHead

        second = self.split(tempHead)

        #calling it self again again till it get to node
        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)

        return self.merge(tempHead, second)

    #spliting into half
    def split(self,tempHead):

        #finding the middle
        fast = slow = tempHead

        while(True):
            
            if fast.next is None:
                break
            
            if fast.next.next is None:
                break
            
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        return temp

    #pushing data
    def push(self,ndata):

        node = Node(data = ndata, next = self.head)

        if self.head is not None:
            self.head.prev = node

        self.head = node

    #traversing data
    def printList(self):
        
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        print()

dll = LinkedList()

dll.push(5)
dll.push(6)
dll.push(7)

dll.printList()

dll.head=dll.mergeSort(dll.head)
dll.printList()
