
# How do you print the first non-repeated character from a string?

class FirstNonRepeated:
    def __init__(self, string):
        self.string = string

    def sol1(self):
        count = 0
        n = len(self.string) - 1
        for i in range(len(self.string)):
            for x in range(i+1, len(self.string)):
                if self.string[i] != self.string[x]:
                    count += 1
                if self.string[i] == self.string[x]:
                    return False
            print(count , n-i)
            if count == n-i:
                return self.string[i]
            else:
                count = 0
        return False

    def sol2(self):
        hashMap = dict()
        for i in self.string:
            hashMap[i] = 1 + hashMap.get(i, 0)

        for key in self.string:
            if hashMap[key] == 1:
                return key

        return -1 


obj = FirstNonRepeated('arsha')
print(obj.sol1())
print(obj.sol2())