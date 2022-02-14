
# SumList: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list

# Example: 7 --> 1 --> 6 + 5 --> 9 --> 2:: 617 + 295 == 919:: 2 --> 1 --> 9


# My approach will be different: I will be collecting all the elements into a string and then adding them up:
# I will make a new ListNode or will overwrite to the odd one,, what is result is bigger than the size l1 or l2?


# O(n) with space: O(n*m)

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
        
        return self.head
    
    def returnState(self):
        res = str()
        cur = self.head
        while cur:
            res += str(cur.data)
            cur = cur.next
        return str(res)

    
    def sumUp(self, num1, num2='0'):
        res = int(num1[::-1]) + int(num2[::-1])
        print(res)
        self.printRes(str(res))
        

    def printRes(self, result=''):
        for x in range(len(str(result))):
            self.add(result[x])

    def printAll(self):
        cur = self.head
        res = str()
        while cur:
            res += str(cur.data) + '--->'
            cur = cur.next
        return res

obj1 = LinkedList()
obj2 = LinkedList()
obj3 = LinkedList()

obj1.add(1);obj1.add(2);obj1.add(3)
obj2.add(4);obj2.add(5);obj2.add(6)

print(obj3.sumUp(obj1.returnState(), obj2.returnState()))
obj3.printRes()
print(obj3.printAll())


