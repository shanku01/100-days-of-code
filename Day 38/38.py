## Day 38 of 100 days of Code
#Binary Tree

"""
Full Binary Tree A Binary Tree is a full binary tree
if every node has 0 or 2 children.

Complete Binary Tree: A Binary Tree is a Complete Binary Tree if all
the levels are completely filled except possibly the last level and the
last level has all keys as left as possible.

Perfect Binary Tree A Binary tree is a Perfect Binary Tree in which all
the internal nodes have two children and all leaf nodes are at the same level.

Balanced Binary Tree 
A binary tree is balanced if the height of the tree is O(Log n) where n is the
number of nodes.

A degenerate (or pathological) tree A Tree where every internal node has one
child.
Such trees are performance-wise same as linked list.
"""

class Node:
    def __init__(self,data=None,right=None,left=None):
        self.left= left
        self.right = right
        self.data = data

#Traversing
def inOrder(node):

    #base case
    if(not node):
        return

    inOrder(node.left)
    print(node.data,end=" ")
    inOrder(node.right)

def insert(node,data):

    #if node is none
    if not node:
        root = Node(data)
        return

    q=[]
    q.append(node)

    while(len(q)):
        node = q[0]
        q.pop(0)

        if(not node.left):
            node.left = Node(data)
            break
        else:
            q.append(node.left)

        if(not node.right):
            node.right = Node(data)
            break
        else:
            q.append(node.right)

# Testing
root = Node(10) 
root.left = Node(11) 
root.left.left = Node(7) 
root.right = Node(9) 
root.right.left = Node(15) 
root.right.right = Node(8) 
 

inOrder(root) 
 

insert(root, 10) 

print() 
inOrder(root)
