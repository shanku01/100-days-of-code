#Day 23 of 100 days of code

##Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class CircularLinkedList:
    def __init__(self):
        self.last = None
 
    # This function is only for empty list
    def addToEmpty(self, data):
 
        # Creating the newnode temp
        temp = Node(data)
        self.last = temp
 
        # Creating the link
        self.last.next = self.last
        return self.last
 
    def addBegin(self, data):
 
        if (self.last == None):
            return self.addToEmpty(data)
 
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
 
        return self.last
 
    def addEnd(self, data):
 
        if (self.last == None):
            return self.addToEmpty(data)
 
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp
 
        return self.last
 
    def addAfter(self, data, item):
 
        if (self.last == None):
            return None
 
        temp = Node(data)
        p = self.last.next
        while p:
            if (p.data == item):
                temp.next = p.next
                p.next = temp
 
                if (p == self.last):
                    self.last = temp
                    return self.last
                else:
                    return self.last
            p = p.next
            if (p == self.last.next):
                print(item, "not present in the list")
                break
 
    def printList(self):
        if (self.last == None):
            print("List is empty")
            return
 
        temp = self.last.next
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.last.next:
                break
        print()

    #Delete Function
    def deleteNode(self,data):

        #base cases
        if self.last == None:
            print("Empty List")
            return

        #if list has only one element
        if self.last == data and self.last.next == self.last:
            self.last = None
            return

        #if head is data
        if self.last.next.data == data:
            self.last.next = self.last.next.next
            return

        temp = self.last.next
        while(temp.next.data!= data):
            temp = temp.next
            if temp.next ==self.last.next:
                print("Data not found")
                return
            
        #skipping the found data
        temp.next = temp.next.next

        return self.last
                    
#Testing

clist = CircularLinkedList()
clist.printList() #Empty

clist.addBegin(4) #At the beginning
clist.addBegin(5)
clist.printList()

clist.addEnd(6) #At the end
clist.printList()

clist.addAfter(6,5)
clist.printList()

clist.deleteNode(5)
clist.printList()

    
                    
                    

        
        
        
