

# Creating a simple trees


# DFS: depth first search algorithm: inorder, preorder, postorder
# BFS: breadth first search algorithm:


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
            print(node.data, end=' ')
            self.inOrder(node.right_child)
        


# 

    def postOrder(self, node):
        # print("PostOrder")
        
        if node:
            self.postOrder(node.left_child)
            self.postOrder(node.right_child)
            print(node.data, end=' ')
        
        


# it print the root first then goes to left and right

    def preOrder(self, node):
        # print("PreOrder")
        
        if node:
            print(node.data, end=' ')
            self.preOrder(node.left_child)
            self.preOrder(node.right_child)
        
        
        

    def searching(self, rootKey, item, count):
        count += 1
        if rootKey is None:
            return False
        elif rootKey.data == item:
            return rootKey.data, count
        elif rootKey.data > item:
            return self.searching(rootKey.left_child, item, count)
        else:
            return self.searching(rootKey.right_child, item, count)

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

    
    def findDuplicates(self, root, seen, res):

        if root:
            if root.data in seen:
                res.append(root.data)
            else:
                seen.add(root.data)
            self.findDuplicates(root.left_child, seen, res)
            self.findDuplicates(root.right_child, seen, res)
            res.append(root.data)
        return res
            
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left_child), self.maxDepth(root.right_child))
        # if root:
        #     maxLDept = self.maxDepth(root.left_child)
        #     maxRDepth = self.maxDepth(root.right_child)
        #     if maxLDept > maxRDepth:
        #         return maxLDept + 1
        #     else:
        #         return maxRDepth + 1
        # else: return -1
    
    def minDepth(self, root):
        if not root: return 0
        if None in [root.left_child, root.right_child]:
            return max(self.minDepth(root.left_child), self.minDepth(root.right_child)) + 1
        else:
            return min(self.minDepth(root.left_child), self.minDepth(root.right_child)) + 1


    def treeBFS(self, root):
        to_visit = []
        if root:
            to_visit.append(root)
            print(root.data, end=' ')
        while to_visit:
            cur = to_visit.pop(0)
            print(cur.data, 'bfs')
            if cur.left_child:
                to_visit.append(cur.left_child)
            if cur.right_child:
                to_visit.append(cur.right_child)

    def searchWithBFS(self, root, val):
        to_visit = []
        if root:
            to_visit.append(root)
        while to_visit:
            cur = to_visit.pop(0)
            print(cur.data, end=' ')
            if cur.data == val:
                return f"{cur.data}=={val}"
            if cur.left_child:
                to_visit.append(cur.left_child)
            if cur.right_child:
                to_visit.append(cur.right_child)

    def remove(self, root, value):
        if not root: return None
        if root.data == value:
            if not root.left_child and not root.right_child: return None
            if not root.left_child and root.right_child: return root.right_child
            if not root.right_child and root.left_child: return root.left_child
            pnt = root.right_child
            while pnt.left_child: pnt = pnt.left_child
            root.data = pnt.data
            root.right_child = self.remove(root.right_child, root.data)

        elif root.data > value:
            self.remove(root.left_child, value)
        else:
            self.remove(root.rigth_child, value)

        return root

root = TreeNode(90)
l = [10, 40, 60, 80, 3, 20, 4, 1, 5, 1, 2, 90, 50, 40, 8]
for i in l:
    root.insert(i)

print(root.searching(root,40, 0))
print(root.maxDepth(root))
print(root.minDepth(root))
print(root.treeBFS(root))
print(root.searchWithBFS(root, 50))
print(root.inOrder(root))

print(root.remove(root, 90))

print(root.inOrder(root))

# print(root.inOrderRemove(root), ': inOrderRemove')

# print(root.minNode(root))
# print(root.maxNode(root))
# seen = set()
# res = list()
# print(root.findDuplicates(root, seen, res))


# print(root.printTree())

# print(root.inOrder(root))
# print(root.postOrder(root))
# print(root.preOrder(root))




# BFS traversal for graphs and trees

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = list()
queue = list()
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        for ne in graph:
            if ne not in visited:
                visited.append(ne)
                queue.append(ne)

print(bfs(visited, graph, 'A'))
    
