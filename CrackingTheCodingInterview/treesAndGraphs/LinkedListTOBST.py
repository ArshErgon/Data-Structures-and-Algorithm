

# Converting a list or a linkedlist to a binary search tree

# Creating linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode


    def printList(self):
        cur = self.head
        res = list()
        while cur:
            res += [cur.data]
            cur = cur.next
        return res


List = LinkedList()
for x in range(1, 10):
    List.push(x)



# Binary Search Tree

class BinarySearchTree:
    def __init__(self, data):
        self.data_root = data
        self.left = None
        self.right = None

    def insert(self, data):
        newNode = BinarySearchTree(data)
        if self.data_root:
            if self.data_root < data:
                if self.left is None:
                    self.left = newNode
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = newNode
                else:
                    self.right.insert(data)
        else:
            self.data_root = data

    
    def preOrder(self, root):
        if root:
            print(root.data_root, end=' ')
            self.preOrder(root.right)
            self.preOrder(root.left)



res_of_linklist = List.printList()
mid = len(res_of_linklist) // 2 

root = BinarySearchTree(res_of_linklist[mid])
for x in res_of_linklist:
    (root.insert(x))
print(root.preOrder(root))



