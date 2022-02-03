

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add(self, item):
        newNode = Node(item)
        if self.head:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode


    def deleteNode(self, valueToDel):
        curr = self.head
        while curr.next != None:
            if curr.next.data == valueToDel:
                curr.next = curr.next.next
            curr = curr.next
        
    def nodePrint(self):
        res = str()
        curr = self.head
        while curr:
            res += str(curr.data) + '---->'
            curr = curr.next
        return res

obj = Linkedlist()

for x in range(1, 21):
    obj.add(x)

print(obj.nodePrint())
print(obj.deleteNode(18))
print(obj.nodePrint())

