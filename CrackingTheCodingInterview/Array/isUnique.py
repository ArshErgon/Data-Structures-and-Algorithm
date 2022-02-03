
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# Questions:
# is the string will be in uppercase or not? do lower case and upper case characters matters? will be there other than chars?
# what if to return? True and False?
# what if the string is empty

# 1. We could have use hashmap and count the occurenece but its not allowed
# 2. We can convert string into a set and then compare the length of new_string_set and string
# 3. Or we can sort the array and then comparing it with two pointers
# 4. the burte force would be looping charaters with for 2 loops with second loop n+1 position
# 5. charaters mapping with [0] * 26 charaters will create a list of 0's * 26



# O(nlogN) with O(1) memory
def isUnique(string):
    sorted_string = sorted(string)
    prev = None
    for i in sorted_string:
        if i == prev:
            return False
        prev = i
    return True

print(isUnique('arsh'))

# O(n^2) with memory O(1)
def isUnique(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
            
    return True

print(isUnique('arsh'))


# O(nlogn) with space O(1)
def isUnique(string):
    string=sorted(string)
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            return False
    return True

print(isUnique('arsh'))

# with sets

def isUnique(string):
    return len(set(string)) == len(string)

print(isUnique('arsh'))


# with hashMaps

def isUnique(string):
    hashMap = dict()
    for i in string:
        hashMap[i] = 1 + hashMap.get(i, 0)

        if hashMap[i] > 1: return False
    
    return True

print(isUnique('arsh'))


# with mapping the characters
# wouldn't work if string is non character

def isUnique(string):
    charMap = [0] * 26

    for i in string.lower():
        pos = ord(i) - ord('a')
        charMap[pos] += 1

    for i in charMap:
        if i > 1:
            return False
    return True

print(isUnique('arsh'))



