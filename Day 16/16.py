#Day 16 of 100 days of code

#Linked List Continue


class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None

        
    #Reverse In a group
    """
    Reverse the first sub-list of size k.
    While reversing keep track of the next node and previous node.
    Let the pointer to the next node be next and pointer to
    the previous node be prev. 
    head->next = reverse(next, k)
    ( Recursively call for rest of the list and link the two sub-lists )
    Return prev ( prev becomes the new head of the list)
    """ 
    def reverseGroup(self, head, k):
       
        if head == None:
          return None
        
        current = head
        next = None
        prev = None
        count = 0
 
        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
 
        # Fixing next
        if next is not None:
            head.next = self.reverseGroup(next, k)
 
        # prev is new head of the input list
        return prev
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

    
    #Reverse a linked list
    """
    Initialize three pointers prev as NULL, curr as head and next as NULL.
    Iterate through the linked list. In loop, do following. 
    Before changing next of current,

    store next node 
    next = curr->next

    Now change next of current

    This is where actual reversing happens 
    curr->next = prev

    Move prev and curr one step forward 
    prev = curr 
    curr = next

    """
    def reverseList(self):
        prev = None
        temp = self.head
        while(temp):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev
 
 
# Code to Run Above
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)

llist.push(1)
 
print ("Given linked list")
llist.printList()
llist.head = llist.reverseGroup(llist.head, 4)
 
print ("\nReversed Linked list")
llist.printList()
