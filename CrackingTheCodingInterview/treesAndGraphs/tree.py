

# Creating a simple trees

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    def insert(self, data):
        newNode = TreeNode(data)
        if self.data:
            if self.data > data:
                if self.left_child is None:
                    self.left_child = newNode
                else:
                    self.left_child.insert(data)
            else:
                if self.right_child is None:
                    self.right_child = newNode
                else:
                    self.right_child.insert(data)
        else:
            self.data = data

    
    def printTree(self):
        if self.left_child:
            self.left_child.printTree()
        print(self.data)
        if self.right_child:
            self.right_child.printTree()

        
    def inOrder(self, node):
        # print("inOrder")
        if node:
            self.inOrder(node.left_child)
            print(node.data)
            self.inOrder(node.right_child)


# 

    def postOrder(self, node):
        # print("PostOrder")
        if node:
            self.postOrder(node.left_child)
            self.postOrder(node.right_child)
            print(node.data)


# it print the root first then goes to left and right

    def preOrder(self, node):
        # print("PreOrder")
        if node:
            print(node.data)
            self.preOrder(node.left_child)
            self.preOrder(node.right_child)
        

    def searching(self, rootKey, item):
        if rootKey is None:
            return False
        elif rootKey.data == item:
            return rootKey.data
        elif rootKey.data > item:
            return self.searching(rootKey.left_child, item)
        else:
            return self.searching(rootKey.right_child, item)

    def minNode(self, rootKey):
        minVal = float('infinity')
        cur = rootKey
        while cur:
            minVal = min(cur.data, minVal)
            cur = cur.left_child
        return minVal

    
    def maxNode(self, rootKey):
        maxVal = 0
        cur = rootKey
        while cur:
            maxVal = max(maxVal, cur.data)
            cur = cur.right_child
        return maxVal
            

root = TreeNode(90)
l = [10, 40, 60, 80, 3, 20, 4, 1, 5]
for i in l:
    root.insert(i)

print(root.searching(root, 1))
print(root.minNode(root))
print(root.maxNode(root))


# print(root.printTree())

# print(root.inOrder(root))
# print(root.postOrder(root))
# print(root.preOrder(root))
