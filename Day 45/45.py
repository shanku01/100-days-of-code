# Day 45 of 100 Days of Code

# Getting postorder traversal from pre and inorder

def search(arr, x, n):

    for i in range(n):
        if (arr[i]==x):
            return i

    return -1

def getPostorder(inorder, preorder, n):

    root = search(inorder,preorder[0],n)

    if (root!= None):
        getPostorder(inorder,preorder[1:n],root)

    if(root != n-1):
        getPostorder(inoder[root+1:n],preoder[root+1:n],n-root-1)

    print(pre[0],end='')

# Testing

In = [ 4, 2, 5, 1, 3, 6 ]
pre = [ 1, 2, 4, 5, 3, 6 ]
n = len(In)
 
print("Postorder Traversal")
 
printPostOrder(In, pre, n)
