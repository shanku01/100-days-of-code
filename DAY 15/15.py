#DAY 15 of 100 DAYS OF CODE

#Linked List continue

#Node class
class Node:
    #Inializing node
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    #Inializing List
    def __init__(self):
        self.head = None

    #Pushing data at head postion    
    def push(self,newData):
        newNode= Node(newData)
        newNode.next = self.head
        self.head = newNode

    #Finding Nth Node
    def findNode(self,index):
        count = 0
        temp = self.head

        #Looping till end
        while(temp):
            if(count==index): #index match
                return temp.data
            else:
                temp=temp.next
                count+=1
        else:
            return "Index in not found in List"

    # This function prints contents of linked list starting 
    # from the given Node 
    def printList(self): 
        tNode = self.head 
        while tNode != None: 
            print(tNode.data), 
            tNode = tNode.next
        print()

    #Swapping Nodes
    """
    The idea is to first search x and y in the given linked list.
    If any of them is not present, then return. While searching for key1 and key2,
    keep track of current and previous pointers.
    First change next of previous pointers,
    then change next of current pointers. 
    """
    def swapNodes(self,key1,key2):
        if key1==key2:
            return

        #Findinf Current key1 and next prev key1
        prev1 = None
        curr1 = self.head
        while curr1 != None and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        #Findinf Current key2 and next prev key2
        prev2 = None
        curr2 = self.head
        while curr2 != None and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        #if Either of key1 or key2 is absent
        if curr1 == None or curr2 == None:
            return

        #if key 1 is not head
        if prev1 !=None:
            prev1.next = curr2
        #if key1 is head    
        else:
            self.head = curr2

        #if key2 is not head
        if prev2!= None:
            prev2.next = curr1
        #if key2 is head
        else:
            self.head =curr1


        #Swap next
        temp = curr1.next
        curr1.next = curr2.next
        curr2.next =temp


    #pair wise data swipping
    """
    Start from the head node and traverse the list.
    While traversing swap data of each node with its next node’s data.
    """
    def pairSwap(self):
        temp = self.head

        if(temp==None):
            return

        while(temp != None and temp.next != None):
            #if both have same data
            if(temp.data == temp.next.data):
                temp=temp.next.next #jumping to next pair

            else:
                #swapping
                temp.data,temp.next.data = temp.next.data,temp.data
                temp=temp.next.next
        
#Using Above Code
list1 = LinkedList()
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(5)
list1.push(7)
list1.printList()

print("Value of Index is :",list1.findNode(3))

list1.swapNodes(4,3)
list1.printList()

list1.pairSwap()
list1.printList()





        
