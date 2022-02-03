
# Palindrome: Implement a function to check if a linked list is a palindrome.

# how would you check a palindrome in a string? by counting the letters even and odd.
# and by using two pointer approach
# it can done by two ways: 
# create any data structure which can reverse the temp and compare it with original


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode


    def reverseList(self):
        res = str()
        cur = self.head
        while cur:
            res += str(cur.data)
            cur = cur.next

        return res[::-1] == res

obj = LinkedList()
obj.add('a')
obj.add('b')
obj.add('a')

print(obj.reverseList())