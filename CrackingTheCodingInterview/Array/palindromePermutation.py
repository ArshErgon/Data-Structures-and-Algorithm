
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# does this string will have integers?
# what to return? the palindrome word or use boolean?

# Solution: 
# 1. I will be using a dictionary to map strings beacause a palindrome has two common properties in every cases:
# no1. all characters are even: acca
# no2: all characters are even except for one: racecar: odd 'E'

# O(N) with space O(N)

def palindromePermutation(string):
    hashMap = dict()
    for i in string.lower().replace(' ', ''):
        hashMap[i] = 1 + hashMap.get(i, 0)
    
    has_odd = False
    for values in hashMap.values():
        if values % 2 == 1:
            if has_odd:
                return False
            has_odd = True
    return True

print(palindromePermutation('racecar'))
print(palindromePermutation('aab baa'))
