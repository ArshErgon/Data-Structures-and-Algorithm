

# How do you check if two strings are anagrams of each other?

class Anagram:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def sol1(self):
        if len(self.word1) != len(self.word2):
            return False

        return sorted(self.word1) == sorted(self.word2)

    
    def sol2(self):
        if len(self.word1) != len(self.word2):
            return False
        hashMap1 = dict()
        hashMap2 = dict()
        for i in range(len(self.word1)):
            word1 = self.word1[i]
            word2 = self.word2[i]
            hashMap1[word1] = 1 + hashMap1.get(word1, 0)
            hashMap2[word2] = 1 + hashMap2.get(word2, 0)

        for key in hashMap1:
            if hashMap1[key] != hashMap2.get(key, 0):
                return False
        return True


    def sol3(self):
        if len(self.word1) != len(self.word2):
            return False

        word1_map = [0] * 26
        word2_map = [0] * 26

        for i in range(len(self.word1)):
            word1 = self.word1[i]
            word2 = self.word2[i]
            pos_1 = ord(word1) - ord('a')
            word1_map[pos_1] += 1
            pos_2 = ord(word2) - ord('a')
            word2_map[pos_2] += 1

        for i in range(len(word1_map)):
            if word1_map[i] != word2_map[i]:
                print(word1_map[i], word2_map[i])
                return False
        return True

word1 = "arh"
word2 = 'arh'

obj = Anagram(word1, word2)
print(obj.sol1())
print(obj.sol2())
print(obj.sol3())
