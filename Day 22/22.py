## Day 22 of 100 days of code

#Circular Linked List Continues

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    #Printing List checking till entry point
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data)
                temp = temp.next
                if(temp == self.head):
                    break
    
    def sortedPush(self,data):
        temp = self.head

        node = Node(data)

        #Base Case
        if self.head == None:
            self.head = node
            node.next = self.head
            return
        
        elif(temp.data>=node.data):
            #if node is smallest in the list

            while temp.next != self.head:
                temp = temp.next

            temp.next = node
            node.next = self.head
            self.head = node

        else:
            #insertion in somewhere middle
        
            while(temp.next != self.head and temp.next.data<node.data):
                temp = temp.next

            node.next = temp.next
            temp.next = node

#Checking if any list is circular or not
def checkList(head):

    #Base case
    if head is None:
        return True

    node = head.next

    while(node is not None and node is not head):
        node = node.next

    #If node == head than Circular if not then not
    return (node == head)

    

#testing
clist = CircularLinkedList()

clist.sortedPush(1)
clist.sortedPush(4)
clist.sortedPush(2)
clist.sortedPush(7)
clist.sortedPush(9)
clist.sortedPush(0)

clist.printList()

#checking list
print(checkList(clist.head))
            

