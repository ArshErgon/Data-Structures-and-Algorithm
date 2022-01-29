
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# will the string in lower case or upper case?
# what if input is empty string?
# do numbers also matters? can integer happen in it?


# Solution:

# 1. Brute force will be sorting every char in str1 and str2 then start a loop and compare each char by char
# 2. Uses of HashMaps to count the occurenece in both str1 and str2


# O(nlogn) with space: O(N)

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1_list_sort = sorted(str1)
    str2_list_sort = sorted(str2)

    for i in range(len(str1_list_sort)):
        if str1_list_sort[i] != str2_list_sort[i]:
            return False

    return True


print(checkPermutation('arsh', 'hrsa'))



# O(n) with memory: O(n)
# hashMaps

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    hashMap_str1, hashMap_str2 = dict(), dict()
    for i in range(len(str1)):
        idx_str1, idx_str2 = str1[i], str2[i]
        hashMap_str1[idx_str1] = 1 + hashMap_str1.get(idx_str1, 0)
        hashMap_str2[idx_str2] = 1 + hashMap_str2.get(idx_str2, 0)

    for i in hashMap_str1:
        if hashMap_str1[i] != hashMap_str2.get(i, 0): # to deal with key error
        # if hashMap_str1[i] != hashMap_str2[i]:
            return False
    return True


print(checkPermutation('arsh', 'arhs'))


# Another solution with using one map

def checkPermutation(str1, str2):
    hashMap = dict() 
    for i in str1:
        hashMap[i] = 1 + hashMap.get(i, 0)

    for v in str2:
        if v in hashMap:
            hashMap[v] -= 1
            if hashMap[v] == 0:
                del hashMap[v]
        else:
            return False
    return len(hashMap) == 0
    
print(checkPermutation('arsh', 'arhs'))




# O(n) with memory O(n)

# hashSets

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1_set = set(str1)
    str2_set = set(str2)
    return str1_set == str2_set

print(checkPermutation('arsh', 'rahs'))
    
