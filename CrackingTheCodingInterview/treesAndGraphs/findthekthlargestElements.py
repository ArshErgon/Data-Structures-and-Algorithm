

# Find the kth largest element in the Binary Search Tree




class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def push(self, data):
        newNode = BinarySearchTree(data)
        if self.data != data:
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


    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end=' ')
            self.inOrder(root.right)

        else:
            return "No root!"


    def findingTheKthNum(self, k):
        k_th_largest_num = list()
        def sol(root):
            if root and len(k_th_largest_num) < k:
                sol(root.right)
                if len(k_th_largest_num) < k:
                    k_th_largest_num.append(root.data)
                    sol(root.left)
        sol(root)
        return k_th_largest_num

    def convertingAlistToBST(self, arrList):
        if arrList:
            mid = len(arrList) // 2
            TreeNode = BinarySearchTree(arrList[mid])
            TreeNode.left = self.convertingAlistToBST(arrList[:mid])
            TreeNode.right = self.convertingAlistToBST(arrList[mid+1:])
            return self.inOrder(TreeNode)


root = BinarySearchTree(30)
for x in range(1, 40):
    root.push(x)

print(root.inOrder(root))
print(root.findingTheKthNum(10))

x = list(range(30, 90))
print(root.convertingAlistToBST(x))