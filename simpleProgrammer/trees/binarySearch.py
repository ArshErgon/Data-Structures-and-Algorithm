

# How do you perform a binary search in a given array?

class BinarySearch:
    def __init__(self, data, target):
        self.data = data
        self.target = target

    def search(self):
        l, r = 0, len(self.data) - 1
        while l <= r:
            mid = (l+r) // 2
            if self.data[mid] == self.target:
                return mid
            elif self.data[mid] > self.target:
                r = mid - 1
            else:
                l = mid + 1
        return -1 

obj = BinarySearch([1,2,3,4,5,6,7,8,9,10], 9)
print(obj.search())