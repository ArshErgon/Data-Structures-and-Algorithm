class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None


n1 = Node('Root Node')

n2 = Node('Left Child')
n3 = Node('Right Child')

n4 = Node('left_grand_child')

n1.left_child = n2
n1.right_child = n3

n1.left_child.left_child = n4

current = n1
while current:
    print(current.data)

    current = current.left_child


# print(n1, n3, n4)
