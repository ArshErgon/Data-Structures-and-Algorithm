
# is anagram leetcode

def isAnagram(word1, word2):
    # ==================
    word1_index = [0] * 26
    word2_index = [0] * 26

    if len(word1) != len(word2):
        return False

    for i in range(len(word1)):
        pos_word1 = ord(word1[i]) - ord('a')
        pos_word2 = ord(word2[i]) - ord('a')
        word1_index[pos_word1] +=  1
        word2_index[pos_word2] +=  1

    print(word1_index, word2_index)

    for i in range(len(word1)):
        if word1_index[i] != word2_index[i]:
            return False
    return True
    # ===================

    hashMap_word1 = dict()
    hashMap_word2 = dict()

    if len(word1) != len(word2):
        return False

    word1, word2 = word1.lower(), word2.lower()

    for i in range(len(word1)):
        hashMap_word1[word1[i]] = 1 + hashMap_word1.get(word1[i], 0)
        hashMap_word2[word2[i]] = 1 + hashMap_word2.get(word2[i], 0)

    for key in hashMap_word1:
        if hashMap_word1[key] != hashMap_word2.get(key, 0):
            return False
    return True
    # ===========

l = []
word1 = "anagram"
word2 = "nagaram"
# print(isAnagram(word1, word2))
print(isAnagram(word1, word2))


# two Sum LeetCode

def twoSum(arrList, target):
    # Brute force
    for i in range(len(arrList)):
        for x in range(1, len(arrList)):
            if arrList[i] + arrList[x] == target:
                return [i, x]
    return [0, 0]

# ======================
# dict is useful in this

    hashMap = dict()

    for key, value in enumerate(arrList):
        diff = target - value
        if diff in hashMap:
            return [hashMap[diff], key]
        hashMap[value] = key
    return hashMap

# =====================

    # wouldn't work if many cases

    prev_prt, next_prt = 0, 1

    for i in range(len(arrList)-1):
        pair_sum = arrList[prev_prt] + arrList[next_prt]

        if pair_sum == target:
            return [prev_prt, next_prt]
        prev_prt += 1
        next_prt += 1
    return False
    
# print(twoSum([1,2,3,4], 4))


# maximum subarray leetcode

def maxSubarr(arrList):
    maxCount = arrList[0]
    subSum = 0

    for i in arrList:
        if subSum < 0:
            subSum = 0
        subSum += i
        maxCount = max(maxCount, subSum)
    return maxCount

# print(maxSubarr([-2,1,-3,4,-1,2,1,-5,4]))


# two sum leetcode 

def twoSum(arrList, target):
    l, r = 0, len(arrList) - 1
    while l < r:
        curSum = arrList[l] + arrList[r]
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l+1, r+1]

# print(twoSum([3,2,4], 6))


# House Robber leetCode

def houseRobber(arrList):
    rob1, rob2 = 0, 0
    for i in arrList:
        print(i+rob1, rob1, rob2)
        temp = max(i + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

print(houseRobber([1,2,3,1]))
