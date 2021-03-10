## Day 31 of 100 days

# Doubly Linked List


class Node:  
    def __init__(self,data):  
        self.data = data  
        self.next = None
        self.prev = None

def deleteNode(head, delete): 
    # base case  
    if (head == None or delete == None): 
        return None
  
    if (head == delete): 
        head = delete.next

    # Change next only if node to be deleted  
    if (delete.next != None): 
        delete.next.prev = delete.prev 
  
    # Change prev only if node to be deleted  
    if (delete.prev != None): 
        delete.prev.next = delete.next
   
    delete = None
    return head 
  

def deleteAllOccurOfX(head, x): 
    # if list is empty  
    if (head == None): 
        return
  
    current = head 
  
    # traverse the list up to the end  
    while (current != None): 
  
        # if node found   
        if (current.data == x): 
   
            next = current.next #Holding next
    
            head = deleteNode(head, current) 
   
            current = next #updating current
          
        else: 
            current = current.next
      
    return head 
   
def push(head,new_data): 

    # allocate node  
    new_node = Node(new_data) 
    new_node.data = new_data 
   
    new_node.prev = None
    new_node.next = head 
  
    if (head != None): 
        head.prev = new_node 
  
    head = new_node 
    return head 
  

def printList(head): 
    # if list is empty  
    if (head == None): 
        print("Dlist empty") 
  
    while (head != None) : 
        print(head.data,end=" ") 
        head = head.next

#Testing

head = None

head = push(head, 2) 
head = push(head, 5) 
head = push(head, 2) 
head = push(head, 4) 
head = push(head, 8) 
  
    
printList(head)

print()
  
x = 2

head = deleteAllOccurOfX(head, x) 

printList(head) 


