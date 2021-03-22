# Day 42 of 100 daysof code

# Inorder traversal on loop

class Node:
    def __init__(self,data = None,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# using loop to travese inorderly
def inOrder(root):

    temp = root #Intiaizing temp to itrate
    stack = [] #to keep data

    while True:
        
        if temp is not None:
            stack.append(temp)

            #gonna check for all left first
            temp = temp.left

        elif(stack):
            temp = stack.pop()
            print(temp.data)

            #gonna check for all right
            temp = temp.right

        else:
            break
    print()


#Testing

# Testing
leaf1 = Node(0)
leaf2 = Node(1)
leaf3 = Node(2)
leaf4 = Node(3)

node1 = Node(4,leaf1,leaf2)
node2 = Node(5,leaf3,leaf4)

root = Node(6,node1,node2)

print("Inorder")
inOrder(root)
    
    
