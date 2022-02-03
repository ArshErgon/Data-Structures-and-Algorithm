
# String Rotation:Assume you have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")



# 1. I think sorting both of them and then comparing i with j will help, but the worse case would be quite high
# 2. Using a dictionary like we use it in anagram... dict for both of them
# 3. using a set for quick lookUp O(1)


# O(n) with O(n) memory

def stringRotation(word1, word2):
    if len(word1) != len(word2):
        return False
    word1_set = set(word1)
    for i in word2:
        if i not in word1_set:
            return False
    return True

print(stringRotation('waterbottle', 'erbottlewat'))