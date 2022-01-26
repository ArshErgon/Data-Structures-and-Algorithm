

# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time


# O(N) with O(1) operations
class StackArr:
    def __init__(self):
        self.stack = []
        self.minNum = float('infinity')

    def add(self, data):
        if data < self.minNum:
            self.minNum = data
        self.stack.insert(0, data)
    
    def poping(self):
        return self.stack.pop(0)
    
    def minNumF(self):
        return self.minNum

    def show(self):
        return self.stack

obj = StackArr()
for x in range(1, 11):
    (obj.add(x))
print(obj.poping())
print(obj.minNumF())
print(obj.show())