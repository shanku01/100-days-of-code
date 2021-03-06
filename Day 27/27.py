## Day 27 of 100 days of code


##Doubly Linked List

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
             
        new_node = Node(data = new_data,next=self.head)
     
        if self.head is not None:
            self.head.prev = new_node
            
        self.head = new_node
 
    def printList(self):
        node = self.head
        while(node is not None):
            print(node.data)
            node = node.next
        print()

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

            
dlist = DoublyLinkedList()

dlist.push(1)
dlist.push(2)
dlist.push(3)

dlist.printList()

dlist.reverse()
dlist.printList()


    
