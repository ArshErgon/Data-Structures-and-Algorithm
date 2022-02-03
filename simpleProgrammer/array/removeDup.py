

# How are duplicates removed from a given array in Java?


class RemoveDup:
    def __init__(self, data):
        self.data = data
    # O(N)
    def sol1(self):
        return set(self.data)
    # O(N), O(1)
    def sol2(self):
        self.data.sort()
        next_prt = 1
        for i in range(1, len(self.data)):
            if self.data[i-1] != self.data[i]:
                self.data[next_prt] = self.data[i]
                next_prt += 1
        return self.data[:next_prt]

obj = RemoveDup([1,2,3,4,5,6,7,6,7,8])
print(obj.sol1(), obj.sol2())