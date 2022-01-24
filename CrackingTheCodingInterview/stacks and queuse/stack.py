

# Stacks Last in first out

# Implementation

class StackArr:
    def __init__(self):
        self.stack = []
    
    def add(self, item):
        return self.stack.insert(0, item)

    def poping(self):
        return self.stack.pop(0)

    def isEmpty(self):
        return self.stack == []
    
    def peek(self):
        return self.stack[0]
    
    def show(self):
        return self.stack

obj = StackArr()
print(obj.add(12))
print(obj.add(13))
print(obj.add(15))
print(obj.poping())
print(obj.isEmpty())
print(obj.peek())
print(obj.show())