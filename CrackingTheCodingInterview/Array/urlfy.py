
# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)


# Questions: What if the string has leading or tailing spaces? should I have to add %20 at ending and starting spaces too?
# what if the inputted string is empty? should I return "%20?"
# how am I going to get the input? in a string type or in list string form?


# O(n) with O(n) memory

def urlify(string):
    str_list = string.lower().split()
    res = str_list[0]
    for i in range(1, len(str_list)):
        res += '%20' + str_list[i]
    
    return res

print(urlify('arsh ergon hey'))