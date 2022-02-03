
# How do you find the duplicate number on a given integer array?

# is the array would be sorted? 
# what I have to return? True or just the duplicate elements 


class FindDup:
    def bruteForce(self, listData): # O(N^2)
        for x in range(len(listData)):
            for i in range(x+1, len(listData)-1):
                if listData[x] == listData[i]:
                    return "Duplicate Found", listData[i], listData[x]

        return -1
    
    def sol2(self, listData): # O(N), O(N)
        seen = set()
        for i in listData:
            if i in seen:
                return "Duplicate"
            seen.add(i)
        return -1 

    # O(nlogn) we can use a binary search but still it would be nlogn because we are sorting it
    def sol3(self, listData):
        listData.sort()
        for i in range(1, len(listData)):
            if listData[i-1] == listData[i]:
                return "Duplicate"
        return -1 

obj = FindDup()
print(obj.bruteForce([1,2,3,4,1,5]))
print(obj.sol2([1,2,3,4,1,5]))
print(obj.sol3([1,2,3,4,1,5]))

