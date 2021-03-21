# Day 42 of 100 daysof code

# Tree traverasal

# Initializing Tree Node
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data

# InOrderTraversing
def traverseInorder(root):

    if root:

        #check for all left
        traverseInorder(root.left)

        #Print Node
        print(root.data)

        #check all right
        traverseInorder(root.right)


# Postorder
def traversePostorder(root):

    if root:

        #check all left
        traversePostorder(root.left)
        
        #check all right
        traversePostorder(root.right)

        #print node
        print(root.data)


# Preorder
def traversePreorder(root):

    if(root):

        #print Node
        print(root.data)

        #check left
        traversePreorder(root.left)

        #check right
        traversePreorder(root.right)


# Testing
leaf1 = Node(0)
leaf2 = Node(1)
leaf3 = Node(2)
leaf4 = Node(3)

node1 = Node(4,leaf1,leaf2)
node2 = Node(5,leaf3,leaf4)

root = Node(6,node1,node2)

print("Inorder")
traverseInorder(root)

print("\nPostorder")
traversePostorder(root)

print("\nPreorder")
traversePreorder(root)

