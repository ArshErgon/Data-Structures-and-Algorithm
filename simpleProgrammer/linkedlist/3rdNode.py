
# Print the third node in linkedlist


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
        while cur:
            print(cur.data, end=' ')
            cur = cur.next 

    def thirdNode(self):
        cur = self.head 
        fast, slow = self.head.next.next, self.head
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        return slow.data

obj = LinkedList()
for x in range(20):
    (obj.push(x))
print(obj.printShow())
print(obj.thirdNode())
