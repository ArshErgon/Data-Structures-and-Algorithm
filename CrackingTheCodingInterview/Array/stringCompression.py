
# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


# first we have to deal with lower cases then uppercase
# we can't use hashmaps for this because hashmaps will place every chars at the same place,,.... maybe with a stack it will work.
# we have to return the "string compression" means if "aaabbccda": a3b2c2d1a1 in this cases, return the original string
# because compression > originalString


#  that last_add_char adds the last chars left becuase my algorithm works when the prev != next_char
#  so if it dont find any new next_char its not gonna add that last chars
# eg: if "aabbcc" it will print a2b2 not c2 because it didnt find new char.. that last_add_char handle this corner case


# O(N) memory: O(n)
def stringCompress(string):
    compress_str = str()
    cnt = 0
    prev = string[0]
    for i in string:
        if i != prev:
            compress_str += prev+str(cnt)
            cnt = 0
        cnt += 1
        prev = i
    last_add_char = compress_str+prev+str(cnt)
    return last_add_char if len(last_add_char) < len(string) else string

print(stringCompress('aaabbccda'))