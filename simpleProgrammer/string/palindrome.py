
# how do you check if the string is palindrome


class Palindrome:
    def __init__(self, data):
        self.data = data

    def sol1(self):
        return self.data == self.data[::-1]

    def sol2(self): # failed if you have duplicates extra 
        return set(self.data) == set(self.data)

    def sol3(self):
        hashMap = dict()
        for i in self.data:
            hashMap[i] = 1 + hashMap.get(i, 0)
        
        has_odd = False
        for key in hashMap.values():
            if key % 2 == 1:
                if has_odd:
                    return False
                has_odd = True

        return True

obj = Palindrome("aabaa")
print(obj.sol1(), obj.sol2(), obj.sol3())