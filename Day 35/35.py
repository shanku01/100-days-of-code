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
   
def deleteNode(head,key):

    #base case
    if head is None or key is None:
        print("List or Data not found")
        return

    temp = head

    while(temp.data !=key):
        temp=temp.next
        if temp is head:
            print("Data not found")
            return
        
    if temp.next !=temp:
         temp.prev.next = temp.next
         temp.next.prev= temp.prev
    else:
        head = None

    del temp

    return head

def printList(head):
    temp = head
    
    if temp is None:
        print("List is empty")
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
head = push(head,6)
head = push(head,7)
printList(head)


head = deleteNode(head,2)
head = deleteNode(head,4)
head = deleteNode(head,6)
printList(head)

head = deleteNode(head,3)
printList(head)


