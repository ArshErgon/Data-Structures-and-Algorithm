
# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# I was thinking to use two lists. which stores min left and max right. comparing with k or lets name it out key.
# after comparing done we could overwrite the linkedList
# can be done by dummy nodes

# https://www.youtube.com/watch?v=KT1iUciJr4g (a better solution)


# Solution
# O(n) with space: O(n)
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

    def partitionList(self, key):
        min_l, max_l = list(), list()
        cur = self.head
        while cur:
            if cur.data < key:
                min_l.append(cur.data)
            else:
                max_l.append(cur.data)
            cur = cur.next

        new_list = min_l + max_l
        cur = self.head
        for i in new_list:
            cur.data = i
            cur = cur.next        
    

    def printMethod(self):
        res = str()
        cur = self.head
        while cur:
            res += str(cur.data) + '--->'
            cur = cur.next
        return res+'None'


obj = LinkedList()
l = [3, 5, 8, 5, 10, 2, 1, 20, 30]
for i in l:
    obj.add(i)

print(obj.printMethod())
obj.partitionList(5)
print(obj.printMethod())
