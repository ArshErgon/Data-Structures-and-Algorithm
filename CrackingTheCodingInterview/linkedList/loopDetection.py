
# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input:
# Output:
# A -> B -> C -> D -> E -> C [the same C as earlier]
# C

# In simple words we have to find a repeated character
# we can use set here
# or much better fast and slow pointers


# O(n); O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        newNode = Node(item)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode
    
    def checkLoop(self):
        slow, fast = self.head, self.head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow if slow == fast else "No Loop"


obj = LinkedList()
for i in range(1, 7):
    obj.add(i)

print(obj.checkLoop())


# O(n); O(n)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        newNode = Node(item)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode

    def checkLoop(self):
        seen = set()
        cur = self.head
        while cur:
            if cur.data in seen:
                return cur.data
            else:
                seen.add(cur.data)
            cur = cur.next
        return "No loop Found"

obj = LinkedList()
for i in range(1, 7):
    obj.add(i)

obj.add(6)

print(obj.checkLoop())