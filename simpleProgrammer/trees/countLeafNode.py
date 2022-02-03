
# How do you count a number of leaf nodes in a given binary tree?

# leaf nodes, nodes which don't have right and left children


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insertation(self, data):
        newNode = TreeNode(data)
        if data != self.data:
            if self.data:
                if self.data > data:
                    if self.left is None:
                        self.left = newNode
                    else:
                        self.left.insertation(data)
                else:
                    if self.right is None:
                        self.right = newNode
                    else:
                        self.right.insertation(data)
            else:
                self.data = newNode


    
    def preOrder(self, root):
        if root:
            print(root.data, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)
        else:return "No Root"


    def countNode(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return self.countNode(root.left) + self.countNode(root.right)

    
    def countNodeBST(self, root):
        if not root:
            return "No root"
        count = 0
        queue = [root]
        while queue:
            s = queue.pop(0)
            if s.left != None:
                queue.append(s.left)
            if s.right != None:
                queue.append(s.right)
            if s.left == None and s.right == None:
                count += 1
        return count


    def BST(self, root):
        if root:
            to_visit = [root]
        while to_visit:
            cur = to_visit.pop(0)
            print(cur.data, end=' ')
            if cur.left != None:
                to_visit.append(cur.left)
            if cur.right != None:
                to_visit.append(cur.right)
        return to_visit
    

    def SearchWithBST(self, root, key):
        if root:
            to_visit = [root]
        while to_visit:
            cur = to_visit.pop(0)
            if cur.data == key:
                return True
            if cur.left:
                to_visit.append(cur.left)
            if cur.right:
                to_visit.append(cur.right)
        else:
            return "Not Found"


root = TreeNode(30)
for x in range(1, 30):
    root.insertation(x)
print(root.preOrder(root))
print(root.countNode(root))
print(root.countNodeBST(root))
print(root.BST(root))
print(root.SearchWithBST(root, 0))
