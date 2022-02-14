

# How do you find the largest and smallest number in an unsorted integer array?
# will there be negatives?
# can I sort them? how will sorting will help


class LargestAndSmallest:
    def __init__(self, listData):
        self.data  = listData
    # O(N)
    def sol1(self):
        maxNum, minNum, = 0, float('infinity')
        for i in self.data:
            if i > maxNum:
                maxNum = i
            else:
                minNum = i
        return maxNum, minNum
    # O(NlogN)
    def sol2(self):
        self.data.sort()
        return self.data[0], self.data[len(self.data)-1]

    
obj = LargestAndSmallest([1,2,3,4,1,5])
print(obj.sol1(), obj.sol2())
