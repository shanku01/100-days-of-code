## Day 32 of 100 days

# Doubly Linked List

# Code by Shashank Pradhan, Github - shanku01

# Python3 program to find a pair with given sum x.
 
# Structure of node of doubly linked list
class Node:
     
    def __init__(self, x):
         
        self.data = x
        self.next = None
        self.prev = None
 
# Function to find pair whose sum equal to given value x.
def pairSum(head, x):
     
    # Set two pointers
    first = head

    
    # To track if we find a pair or not
    found = False
 
    # The loop terminates when they don't find pair
    while (first):
        second = first
        while(second):
            if(first.data+second.data == x):
                print("(",first.data,",",second.data,")")
                found = True
                first = first.next
            second = second.next
        first= first.next
    # If pair is not present
    if (found == False):
        print("No pair found")
 
# A utility function to insert a new node
# at the beginning of doubly linked list
def insert(head, data):
     
    temp = Node(data)
     
    if not head:
        head = temp
    else:
        temp.next = head
        head.prev = temp
        head = temp
         
    return head
 
# Driver code
if __name__ == '__main__':
     
    head = None
    head = insert(head, 0)
    head = insert(head, 7)
    head = insert(head, 1)
    head = insert(head, 6)
    head = insert(head, 3)
    head = insert(head, 5)
    head = insert(head, 4)
    head = insert(head, 2)
    
    
    x = 7
 
    pairSum(head, x)


