## Day 39 of 100 days of Code

#Binary Tree

#Defining Node for tree
class Node:
    #Intializing data , left node and right node
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

#Traversing inoderly
def inOrder(temp):

    #if node if empty it will reverse
    if(not temp):
        return
    
    inOrder(temp.left)
    print(temp.data,end=" ")
    inOrder(temp.right)



def deleteDeepest(root,dNode):

    #using stack to track 
    q = []
    q.append(root)

    #finding node to be deleted
    while(len(q)):
        temp =q.pop(0)
        
        if temp is dNode:
            temp =None
            return
        
        if temp.right:
            if temp.right is dNode:
                temp.right = None
                return
            else:
                q.append(temp.right)
                
        if temp.left:
            if temp.left is dNode:
                temp.left = None
                return
            else:
                q.append(temp.left)

def deleteKey(root,key):

    #base case
    if root is None:
        return None

    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return None

    #intializing
    dNode = None
    q=[]
    q.append(root)

    #finding Node
    while(len(q)):
        temp = q.pop(0)
        if temp.data ==key:
            dNode=temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    #Deleting Node
    if dNode:
        x = temp.data
        deleteDeepest(root,temp)
        dNode.data = x
        
    return root

#Testing
leaf1 = Node(1)
leaf2 = Node(2)
leaf3 = Node(3)
leaf4 = Node(4)

node1 = Node(5,leaf1,leaf2)
node2 = Node(6,leaf3,leaf4)

root = Node(7,node1,node2)

inOrder(root)
print(" ")

root = deleteKey(root,5)
inOrder(root)

            
    
