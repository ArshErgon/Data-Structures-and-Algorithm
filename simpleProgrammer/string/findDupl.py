
# How do you print duplicate characters from a string?

class FindDuplicate:
    def __init__(self, string):
        self.string = string

    def findDup(self):
        for i in range(len(self.string)):
            for x in range(i+1, len(self.string)):
                if self.string[i] == self.string[x]:
                    return True
        return False

    def sol2(self):
        hashSet = set()
        for i in self.string:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False


    def sol3(self):
        self.string = sorted(self.string)
        for i in range(1, len(self.string)-1):
            if self.string[i-1] == self.string[i]:
                return True
        return False

    def sol4(self):
        seen = [0] * 26
        for i in self.string:
            pos = ord(i) - ord('a')
            seen[pos] += 1
        
        for x in seen:
            if x == 2:
                return True
        return False

obj = FindDuplicate('arsh')
print(obj.findDup(), obj.sol2(), obj.sol3(), obj.sol4())