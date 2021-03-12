## Day 33 of 100 days

# Doubly Linked List

class Node:
    def __init__(self,data=None,next= None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def push(head,ndata):
    node = Node(data=ndata,next = head)

    if head is not None:
        head.prev = node

    head = node
    return head

def printList(head):
    temp = head

    while(temp):
        print(temp.data,end=" ")
        temp = temp.next

    print()

def rotateByN(head,n):

    #base case
    if n == 0:
        return

    temp = head

    count =1
    while(count<n and temp!=None):
        temp = temp.next
        count+=1

    if temp is None:
        return

    p1 = temp #intializing nth node
    
    while temp.next!=None:
        temp = temp.next
        
    #changing head and tail
    temp.next =head 
    head.prev = temp
    head = p1.next
    head.prev = None
    p1.next = None

    return head



#Testing
head = None

head = push(head,"5")
head = push(head,"4")
head = push(head,"3")
head = push(head,"2")
head = push(head,"1")
printList(head)

head=rotateByN(head,3)
printList(head)


    

    
        
