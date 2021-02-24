#Day 17 of 100 Days of code

#Merge Sort Linked List

"""
Merge sort is often preferred for sorting a linked list.
The slow random-access performance of a linked list makes
some other algorithms (such as quicksort) perform poorly,
and others (such as heapsort) completely impossible.
"""

"""
MergeSort(headRef)
1) If the head is NULL or there is only one element in the Linked List 
    then return.
2) Else divide the linked list into two halves.  
      FrontBackSplit(head, &a, &b); /* a and b are two halves */
3) Sort the two halves a and b.
      MergeSort(a);
      MergeSort(b);
4) Merge the sorted a and b (using SortedMerge() discussed here) 
   and update the head pointer using headRef.
     *headRef = SortedMerge(a, b);
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
        head = self.head
        while(head):
            print(head.data)
            head= head.next
        print()

    def getMiddle(self,head):

        if head ==None:
            return head

        middle=head
        last = head
        #when last will reach last middle will be at middle as last moving fast
        while(last.next and last.next.next):
            middle = middle.next
            last = last.next.next

        return middle

    def sortedMerge(self,left,right):
        head = None

        #Base cases
        if left==None:
            return right
        if right == None:
            return left

        #swaping
        if left.data<=right.data:
            head = left
            head.next = self.sortedMerge(left.next,right)
        else:
            head = right
            head.next = self.sortedMerge(left,right.next)

        return head
    

    def mergeSort(self,head):

        #Base case
        if head==None or head.next ==None:
            return head

        middle = self.getMiddle(head)
        middleNext = middle.next
        
        middle.next = None #dividing List

        left = self.mergeSort(head) #sorting first half

        right = self.mergeSort(middleNext) #sorting other half

        sortedList = self.sortedMerge(left,right)

        return sortedList


#Using Code Above

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(5)
llist.push(7)
llist.printList()

llist.head = llist.mergeSort(llist.head)

llist.printList()

        
