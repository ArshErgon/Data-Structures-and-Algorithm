

# How do you find the sum of two linked lists using Stack?

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

    
    def printAll(self):
        cur = self.head 
        while cur:
            print(cur.data, end= ' ')
            cur = cur.next

        
    def mergeAndSum(self, obj1, obj2):
        list1 = list()
        list2 = list()
        while obj1:
            list1.append(str(obj1.data))
            obj1 = obj1.next
        
        while obj2:
            list2.append(str(obj2.data))
            obj2 = obj2.next

        sumList1 = ''.join(list1)
        sumList2 = ''.join(list2)
        return int(sumList1) + int(sumList2)


obj1 = LinkedList()
for x in range(1, 5):
    obj1.push(x)

obj2 = LinkedList()
for x in range(6, 10):
    obj2.push(x)

obj3 = LinkedList()
print(obj3.mergeAndSum(obj1.head, obj2.head))
