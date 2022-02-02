
# How do you count a number of vowels and consonants in a given string?


class CountVowelsAndConstants:
    def __init__(self, data):
        self.data = data
    
    def sol1(self):
        hashMap = dict()
        d = {'a', 'e', 'i', 'o', 'u'}
        for i in self.data:
            hashMap[i] = 1 + hashMap.get(i, 0)

        hashMap_vowels = dict()
        for i in d:
            if i in hashMap:
                hashMap_vowels[i] = hashMap[i]
                del hashMap[i]
        
        return hashMap_vowels, hashMap

obj = CountVowelsAndConstants("arsh ergon")
print(obj.sol1())