
# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

# can be done by two ways or more,,, but with a list or a fast and slow pointer


# with a fast and slow pointers
# O(N) space: O(1)

from re import S


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def add(self, items):
        newNode = Node(items)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode       

    def gettingMiddle(self):
        curr , slow, fast = self.head, self.head, self.head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        while curr.next:
            if curr.next == slow:
                curr.next = curr.next.next
            curr = curr.next
        
        return slow.data

    
    def printMethod(self):
        res = str()
        curr = self.head
        while curr.next:
            res += str(curr.data)+'--->'
            curr = curr.next
        return res

obj = LinkedList()
for x in range(1, 6):
    obj.add(x)
print(obj.printMethod())
print(obj.gettingMiddle())
print(obj.printMethod())



# Solving it by a list
# O(N) space: O(n)

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
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode

    def removeMiddle(self):
        res = list()
        cur = self.head
        while cur.next:
            res.append(cur.data)
            cur = cur.next
        res.pop((len(res))//2)

        return res

    
obj = LinkedList()
for x in range(1, 6):
    obj.add(x)

print(obj.removeMiddle())