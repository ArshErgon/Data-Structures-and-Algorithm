
# How do you check if a string contains only digits?

# will it be alphanumeric?

class isDigit:
    def __init__(self, strDigit):
        self.strDigit = strDigit

    
    def sol1(self):
        return self.strDigit.isdigit()

    def sol2(self):
        d = str({1,2,3,4,5,6,7,8,9,0})
        count = 0 
        for i in self.strDigit:
            if i in d:
                count += 1

        return count == len(self.strDigit)


obj = isDigit("2234") 
print(obj.sol1(), obj.sol2())