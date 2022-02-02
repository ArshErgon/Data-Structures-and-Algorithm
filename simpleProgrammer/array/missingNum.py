
# How do you find the missing number in a given integer array of 1 to 100?

# A brute force would be using an for loop and check is the element is present is there or not, you can use set for O(1) lookUps
# will there be duplicates?


class MissingNumber:
    def findNum(self, listData):
        x = set(listData)
        Sumn = len(listData)

        # return n*(n+1) // 2

obj = MissingNumber()

print(obj.findNum())