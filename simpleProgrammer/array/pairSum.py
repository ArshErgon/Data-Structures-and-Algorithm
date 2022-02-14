

# How do you find all pairs of an integer array whose sum is equal to a given number?
# or Two sum



class TwoSum:
    def __init__(self, listData, target):
        self.data = listData
        self.target = target

    # O(N^2), O(1)
    def sol1(self):
        for i in range(len(self.data)):
            for x in range(i+1, len(self.data)):
                if self.data[i] + self.data[x] == self.target:
                    return self.data[i], self.data[x]

        return [-1, -1]

    # O(N), O(N)
    def sol2(self):
        hashMap = dict()
        for i in self.data:
            diff = self.target - i
            if diff in hashMap:
                return hashMap[diff], i
            hashMap[i] = i
        return [-1, -1], hashMap, diff

obj = TwoSum([1,2,3,4,5], 5)
print(obj.sol1(), obj.sol2())