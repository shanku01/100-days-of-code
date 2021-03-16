## Day 37 of 100 days of Code
#Binary Tree

"""
A tree whose elements have at most 2 children is called a binary tree.
Since each element in a binary tree can have only 2 children,
we typically name them the left and right child.
"""

"""
Main applications of trees include: 
1. Manipulate hierarchical data. 
2. Make information easy to search (see tree traversal). 
3. Manipulate sorted lists of data. 
4. As a workflow for compositing digital images for visual effects. 
5. Router algorithms 
6. Form of a multi-stage decision-making (see business chess). 
"""


class Node:
    def __init__(self,data=None,right=None,left=None):
        self.left= left
        self.right = right
        self.data = data

#Testing

leaf1 = Node(0)
leaf2 = Node (1)
leaf3 = Node(2)
leaf4 = Node (3)

node1 = Node(4,leaf1,leaf2)
node2 = Node (5,leaf3,leaf4)

root = Node(6,node1,node2)

