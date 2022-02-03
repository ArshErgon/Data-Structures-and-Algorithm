
# How do you count the occurrence of a given character in a string?

# if string is "" and I have a key?


class CountOccurence:
    def __init__(self, data, key):
        self.data = data
        self.key = key
    def sol1(self):
        count = 0
        for i in self.data:
            if i == self.key:
                count += 1
        return count 
    
    def sol2(self):
        hashMap = dict()
        for i in self.data:
            hashMap[i] = 1 + hashMap.get(i, 0)
        
        return hashMap[self.key] if self.key in hashMap else -1 


print(CountOccurence("arshergonali", '6').sol1())
print(CountOccurence("arshergonali", '1').sol2())
