## Day 30 of 100 Days of pyhton

# Doubly Linked List

class Node:
    def __init__(self,data=None, next = None, prev = None):

        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def sortedInsert(self,data):

         node = Node(data)

         if self.head is None:
             self.head = node

         elif self.head.data >= node.data:
             node.next = self.head
             node.next.prev = node
             self.head = node

         else:
            current = self.head

            while((current.next is not None) and (current.next.data<node.data)):
                current = current.next

            node.next = current.next

            if current.next is not None:
                node.next.prev = node

            current.next = node
            node.prev = current

    def printList(self):

        node = self.head
        while node:
            print(node.data,end=" ")
            node = node.next

def _deleteNode(head_ref, _del): 
  
    # base case  
    if (head_ref == None or _del == None): 
        return
  
    # If node to be _deleted is head node  
    if (head_ref == _del): 
        head_ref = _del.next
  
    # Change next only if node to be _deleted  
    # is NOT the last node  
    if (_del.next != None): 
        _del.next.prev = _del.prev 
  
    # Change prev only if node to be _deleted  
    # is NOT the first node  
    if (_del.prev != None): 
        _del.prev.next = _del.next
  
    return head_ref 
  
# function to remove duplicates from a  
# sorted doubly linked list  
def removeDuplicates(head_ref): 
  
    # if list is empty  
    if ((head_ref) == None): 
        return None
  
    current = head_ref 
    next = None
  
    # traverse the list till the last node  
    while (current.next != None) : 
  
        # Compare current node with next node  
        if (current.data == current.next.data): 
  
            # _delete the node pointed to by 
            # 'current.next'  
            _deleteNode(head_ref, current.next) 
  
        # else simply move to the next node  
        else: 
            current = current.next
      
    return head_ref

#testing
dlist = DoublyLinkedList()

dlist.sortedInsert(8)
dlist.sortedInsert(7)
dlist.sortedInsert(9)
dlist.sortedInsert(9)

dlist.printList()
print()

dlist.head=removeDuplicates(dlist.head)
dlist.printList()

