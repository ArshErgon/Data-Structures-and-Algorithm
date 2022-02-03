
# making stack with linkedlist


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        newData = Node(data)
        if self.top:
            newData.next = self.top
            self.top = newData
        else:
            self.top = newData
        self.size += 1


    def poping(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None


    def show(self):
        res = str()
        cur = self.top
        while cur:
            res += str(cur.data) + '-->'
            cur = cur.next
        return res

    def peek(self):
        if self.top:
            return self.top.data
        return None

obj = Stack()
for x in range(10):
    obj.push(x)

print(obj.show())
print(obj.poping())
print(obj.show())

print(obj.peek())