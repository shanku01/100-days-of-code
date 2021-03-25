# Day 44 of 100 daysof code

# Morris Traversal

class Node:
    def __init__(self,data = None,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        


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

    
    
