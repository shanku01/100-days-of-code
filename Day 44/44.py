# Day 44 of 100 daysof code

# Morris Traversal

class Node:
    def __init__(self,data = None,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
def morrisTraversal(root):

    temp = root #intializing root

    #travessing every Node
    while temp is not None:

        #checking all left
        if temp.left is None:
            yield temp.data
            temp = temp.right

        else:

            pre = temp.left

            while pre.right is not None and pre.right is not temp:
                pre = pre.right

            if pre.right is None:

                pre.right = temp
                temp = temp.left

            # Checking right
            else:
                pre.right = None
                yield temp.data
                temp = temp.right
                

# Testing
leaf1 = Node(0)
leaf2 = Node(1)
leaf3 = Node(2)
leaf4 = Node(3)

node1 = Node(4,leaf1,leaf2)
node2 = Node(5,leaf3,leaf4)

root = Node(6,node1,node2)

for data in morrisTraversal(root):
    print(data,end="")

    
    
