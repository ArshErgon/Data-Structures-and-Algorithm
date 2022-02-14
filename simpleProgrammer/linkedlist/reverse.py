
# Reverse linkedlist 

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

    def printMethod(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        self.head = prev

obj = LinkedList()
for x in range(1, 21):
    obj.push(x)
print(obj.printMethod())
obj.reverse()
print(obj.printMethod())
