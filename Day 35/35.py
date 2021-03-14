## Day 35 of 100 days of Code

# Circular Doubly Linked List

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


printList(head)

