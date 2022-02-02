
# How is a binary search tree implemented?
# How do you perform preorder traversal in a given binary tree?
 

from logging import root


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    
    def push(self, data):
        newNode = BinarySearchTree(data)
        if data != self.data:
            
            if self.data:

                if self.data > data:
                    if self.left is None:
                        self.left = newNode
                    else:
                        self.left.push(data)
                else:
                    if self.right is None:
                        self.right = newNode
                    else:
                        self.right.push(data)
            else:
                self.data = data


    def preOrder(self, root):
        if root:
            print(root.data, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)
        else:
            return "No ROOT"

    
    def InOrder(self, root):
        if root:
            self.preOrder(root.left)
            print(root.data, end=' ')
            self.preOrder(root.right)
        else:
            return "No ROOT"

    def postOrder(self, root):
        if root:
            self.preOrder(root.left)
            self.preOrder(root.right)
            print(root.data, end=' ')
        else:
            return "No ROOT"

root = BinarySearchTree(10)
for x in range(1, 20):
    root.push(x)

print(root.preOrder(root))
print(root.InOrder(root))
print(root.postOrder(root))
