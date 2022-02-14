
# Queue via Stacks:
# Implement a MyQueue class which implements a queue using two stacks.


class Stacks:
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def add(self, item):
        self.stack.insert(0, item)
    
    def isEmpty(self):
        return len(self.stack) == 0

    def show(self):
        return self.stack

    def reverseStack(self):
        if not self.isEmpty:
            raise RuntimeError("Stack is Empty")
        while len(self.stack):
            self.queue.append(self.stack.pop(0))
    
    def queuePop(self):
        return self.queue.pop()
    
    def showQueue(self):
        return self.queue


obj = Stacks()
for x in range(10, 0, -1):
    print(obj.add(x))
print(obj.show())

print(obj.reverseStack())

print(obj.queuePop())
print(obj.showQueue())