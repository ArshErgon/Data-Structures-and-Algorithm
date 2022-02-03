

# How do you reverse an array in place?

class Reverse:
    def __init__(self, data):
        self.data = data

    def sol1(self):
        right = len(self.data)  - 1
        left = 0
        while left != right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1
        return self.data


    def sol2(self):
        return self.data[::-1]

obj = Reverse([1,2,3,4,5])
print(obj.sol1(), obj.sol2())