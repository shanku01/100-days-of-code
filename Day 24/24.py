## Day 24 of 100 days of Code

#Circular Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def push(self,data):

        node = Node(data)
        
        #base case
        if self.last == None:
            #make the last node and create loop
            self.last = node
            self.last.next = self.last

        #make node last's next and node's next will be head
        node.next = self.last.next
        self.last.next = node

    def countNodes(self):

        #base case
        if self.last == None:
            return "The list is empty"

        #Intalizing head and count
        temp = self.last.next
        count =1

        #looping Till we reach last 
        while(temp!=self.last):
            count+=1
            temp =temp.next

        return count

#Josephus Circle
def getJosephusPostion(m,n):

    #Creating Circular List
    clist = CircularLinkedList()
    for i in range(1,n+1):
        clist.push(i)

    #Intaializing pointers
    p1 = clist.last.next
    p2 = clist.last.next

    while(p1.next != p1):
        count = 1
        while(count!= m):
            p2 = p1
            p1 = p1.next
            count+=1

        p2.next = p1.next

        p1 = p2.next

    print("Joshephus Postion is ",n+1 - p1.data)


    


#testing
clist = CircularLinkedList()

clist.push(1)
clist.push(2)
clist.push(3)
print(clist.countNodes())

print()

clist.push(4)
print(clist.countNodes())

getJosephusPostion(4,14)
        
        
