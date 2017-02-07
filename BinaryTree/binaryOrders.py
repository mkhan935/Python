#Simple program to go over tree traversals

class Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.value = item
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.value)
        printInorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Inorder traversal of the tree is:")
printInorder(root)
