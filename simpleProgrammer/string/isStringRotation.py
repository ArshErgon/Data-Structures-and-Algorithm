
# How do you check if two strings are a rotation of each other?


# 1. Sort them and compare them 
# 2. Map their occurences
# 3. map their position


class IsStringRotation:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def sol1(self):
        return sorted(self.word1) == sorted(self.word2)

    def sol2(self):
        if len(self.word1) != len(self.word2): return False

        mapping_word1 = [0] * 26
        mapping_word2 = [0] * 26

        for i in range(len(self.word1)):
            word1 = ord(self.word1[i].lower()) - ord('a')
            word2 = ord(self.word2[i].lower()) - ord('a')
            mapping_word1[word1] += 1
            mapping_word2[word2] += 1

        for i in range(len(mapping_word1)):
            if mapping_word1[i] != mapping_word2[i]:
                return False

        return True


print(IsStringRotation("arsh", 'rsha').sol2())