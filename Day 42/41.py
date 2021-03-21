# Day 40 of 100 daysof code

#Binary Tree

#Array Implementation of Binary tree

#specifying size
tree =[None]*20

#entering data at root
def root(data):
    if tree[0]!= None:
        print("Root is here")
    
    else:
        tree[0]= data

def setLeft(data,parent):
    if tree[parent]==None:
        print("Can't set child at", (parent * 2) + 1, ", no parent found")
    else:
        tree[(parent*2)+1]=data

def setRight(data,parent):
    if tree[parent]==None:
        print("Can't set child at", (parent * 2) + 2, ", no parent found")
    else:
        tree[(parent*2)+2]=data

def traverse():
    for i in range(20):
        if tree[i]!=None:
            print(tree[i],end="")
        else:
            print("-",end="")
    print()

#Test
root('A')
setRight('C', 0)
setLeft('D', 0)
setRight('E', 1)
setRight('F', 1)
traverse()


