
# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# I'm thinking to use a list to store the data and using a -k for getting the kth last element, lookup would O(1)...
# Because i will be doing -k from the last of the array, getting it with its index

# its has to be a better answer
#  its by using fast pointer and a slow pointer like we do in finding middle of the linked list with fast and slow


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
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode


    def gettingKthElem(self, k):
        slow_ptr, fast_ptr = self.head, self.head
        for _ in range(k):
            if not fast_ptr:
                return None
            fast_ptr = fast_ptr.next
        
        while fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return slow_ptr.data

obj = LinkedList()
for x in range(11):
    obj.add(x)

print(obj.gettingKthElem(2))




# solution with the help of list
# O(n) with space:o(n)
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

    def gettingKthElem(self, k):
        res = list()
        curr = self.head
        while curr.next:
            res.append(curr.next.data)
            curr = curr.next
        
        return res[-k]

obj = LinkedList()
for x in range(10):
    obj.add(x)

print(obj.gettingKthElem(3))



