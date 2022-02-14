
# Queues first in first out

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)
    
    def poping(self):
        return self.queue.pop()
    
    def peek(self):
        return self.queue[-1]
    
    def isEmpty(self):
        return self.queue == []
    
    def show(self):
        return self.queue

obj = Queue()
obj.add(10)
obj.add(12)
obj.add(13)
print(obj.poping())
print(obj.peek())
print(obj.isEmpty())
print(obj.show())


