
# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# The three edits:
# remove, replace, and insert




# O(N) with O(1)

def oneAway(word1, word2):
    if abs(len(word1)-len(word2)) > 1:
        return False
    
    flag = False
    i= 0
    while i < len(word1):
        if word1[i] != word2[i]:
            if not flag:
                flag = True
                i += 1
            else:
                return False
        else:
            i += 1
    return True

print(oneAway('arsh', 'afsh'))