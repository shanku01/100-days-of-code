## Day 29 of 100 days of code

#Doubly Linked List

class Node:
     
    def __init__(self, x):
         
        self.data = x
        self.next = None
        self.prev = None
 
# Function to find pair whose sum 
# equal to given value x.
def pairSum(head, x):

    first = head
    second = head
     
    while (second.next != None):
        second = second.next
 
    # To track if we find a pair or not
    found = False
 
    # The loop terminates when either of 
    # two pointers become None, or they
    # cross each other (second.next == 
    # first), or they become same 
    # (first == second)
    while (first != None and second != None and
           first != second and second.next != first):
             
        # Pair found
        if ((first.data + second.data) == x):
            found = True
            print("(", first.data, ",",
                       second.data, ")")
            
            first = first.next
             
            second = second.prev
        else:
            if ((first.data + second.data) < x):
                first = first.next
            else:
                second = second.prev
 
    # If pair is not present
    if (found == False):
        print("No pair found")
 

def push(head, data):
     
    temp = Node(data)
     
    if not head:
        head = temp
    else:
        temp.next = head
        head.prev = temp
        head = temp
         
    return head

#Testing
head = None

head = push(head,9)
head = push(head,10)
head = push(head,11)
head = push(head,12)
head = push(head,9)
head = push(head,10)
head = push(head,11)
head = push(head,12)


pairSum(head,21)
            
        
