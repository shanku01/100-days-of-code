#Day 19 of 100 days of code

#Removing Loops
"""
This method is also dependent on Floyd’s Cycle detection algorithm.
Detect Loop using Floyd’s Cycle detection algorithm and get the pointer
to a loop node.
Count the number of nodes in loop. Let the count be k.
Fix one pointer to the head and another to a kth node from the head.
Move both pointers at the same pace, they will meet at loop starting node.
Get a pointer to the last node of the loop and make next of it as NULL.
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

    def detectAndRemoveLoop(self):
        slowP = fastP = self.head

        while(slowP and fastP and fastP.next):
            slowP = slowP.next
            fastP = fastP.next.next

            if slowP ==fastP:
                self.removeLoop(slowP)

                return "Loop found and sorted"
        return "No loop found"

    def removeLoop(self,loopN):

        #Iniliazing pointers
        p1 = loopN
        p2 = loopN
        
        #finding lengeth of loop
        k = 1
        while(p1.next != p2):
            p1 =p1.next
            k+=1

        p1 = self.head

        #moving other pointer at k node
        p2 = self.head
        for i in range(k):
            p2 = p2.next
            
        #finding start of loop
        while(p2 != p1):
            p1 = p1.next
            p2 = p2.next

        #finding end of the loop
        while(p2.next !=p1):
            p2 = p2.next

        #removing loop
        p2.next = None

    def modifiedRemoveLoop(self):
 
        if self.head is None:
            return
        if self.head.next is None:
            return
 
        slow = self.head
        fast = self.head
 
        # Move slow and fast 1 and 2 steps respectively
        slow = slow.next
        fast = fast.next.next
 
        # Search for loop using slow and fast pointers
        while (fast is not None):
            if fast.next is None:
                break
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
 
        # if loop exists
        if slow == fast:
            slow = self.head
            while (slow.next != fast.next):
                slow = slow.next
                fast = fast.next
 
            # Sinc fast.next is the looping point
            fast.next = None  # Remove loop

        
            
        

#Testing
list1 = LinkedList()
list1.push(0)
list1.push(2)
list1.push(2)
list1.push(4)
list1.push(5)
list1.push(6)
list1.printList()

#creating loop for test
list1.head.next.next.next.next.next.next = list1.head.next.next
list1.detectAndRemoveLoop()
list1.printList()


list1.head.next.next.next.next.next.next = list1.head.next.next
list1.modifiedRemoveLoop()
list1.printList()
