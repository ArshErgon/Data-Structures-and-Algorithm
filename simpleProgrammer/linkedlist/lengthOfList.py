
# Finding the length of a singly linkedlist


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
        
    def printShow(self):
        cur = self.head
        count = 0
        while cur:
            # print(cur.data, end=' ')
            cur = cur.next
            count += 1
        return count


obj = LinkedList()
for x in range(10):
    obj.push(x)

print(obj.printShow())

    