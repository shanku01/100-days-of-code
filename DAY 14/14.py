#DAY 14 0F 100 DAYS OF CODE

#Linked List Continue


class Node:
    def __init__(self, data=None):
        self.data =data
        self.next= None

class LinkedList:

    #initalizing head
    def __init__(self):
        self.head = None


    #Inserting at Begining
    def push(self, newData):
        newNode = Node(newData)
        newNode.next  = self.head
        self.head = newNode

    #Deleting Linked List at a given position
    """
    If the node to be deleted is the root, simply delete it.
    To delete a middle node, we must have a pointer to the node previous to
    the node to be deleted. So if positions are not zero,
    we run a loop position-1 times and get a pointer to the previous node.
    """
    def deleteNode(self,position):

        #checking if it's empty
        if self.head ==None:
            print("List is empty \n")
            return

        #storing head
        temp = self.head

        #Position is head
        if position ==0:
            self.head = temp.next
            temp =None
            return

        #Finding Position
        for i in range(position-1):
            temp = temp.next
            if temp or temp.next is None:
                print("List doesn't have that postion \n")
                return
            
        
        #Postion found
        next= temp.next.next #creating next
        
        temp.next =None #deleting node

        temp.next = next #unlicking the node

    #Print Linked List
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp =temp.next
        print("")

    #Finding Length
    """
    Pointer need to be used to get the length
    """
    def listLength(self):
        temp = self.head
        count =0
        while (temp):
            count+=1
            temp =temp.next
        return count

    #Finding element
    def findElement(self,key):
        temp = self.head
        while(temp):
            if(temp.data==key):
                print("Element Found \n")
                return
            temp=temp.next
        print("Element not Found \n")
        return
        
                        

#Using above Codes

list1 = LinkedList()
list1.push(6)
list1.push(3)
list1.push(2)
list1.push(1)

list1.printList() #print List

list1.deleteNode(0) #delting List

list1.printList() #print List

#Deleting Linked List
"""
In Python, automatic garbage collection happens,
so deleting a linked list is easy. Just need to change head to null.
"""
list1.head = None
list1.push(5)
list1.push(6)
list1.printList() #print List

print(list1.listLength(),"\n") #getting length

list1.findElement(6)
list1.findElement(1)









        

        
        
