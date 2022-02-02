
# Find the middle element of a linkedlist


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

    def printOption(self):
        res = str()
        cur = self.head
        while cur:
            res += str(cur.data)+'-->'
            cur = cur.next
        return res

    def middleElement(self):
        fast, slow= self.head.next, self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data

obj = LinkedList()
for x in range(1, 20):
    obj.push(x)
print(obj.middleElement())
print(obj.printOption())