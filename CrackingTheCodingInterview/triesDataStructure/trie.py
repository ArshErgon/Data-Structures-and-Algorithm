

# Trie for word searching. text complitation 

class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()


    def _charToIndex(self, ch):
        #  print(ord(ch)-ord('a'), ch)
        return ord(ch)-ord('a')

    
    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord

    def hasAChild(self):
        pCrawl = self.root
        for i in range(26):
            if pCrawl.children[i]:
                return True
        return False
    
    def printKeys(self):
        res = list()
        pCrawl = self.root
        # print(dir(pCrawl))
        self.printAllKeys(pCrawl, res)

    def printAllKeys(self, root, res):
        if root.isEndOfWord == True:
            print(''.join(res))
        for i in range(26):
            if root.children[i] is not None:
                ch = chr(97+i)
                res.append(ch)
                self.printAllKeys(root.children[i], res)
                res.pop()



if __name__ == '__main__':
    keys = ["the","a","there","answer","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]

    t = Trie()
    for key in  keys:
        t.insert(key)

    # print("{} ---- {}".format("the",output[t.search("the")]))
    # print("{} ---- {}".format("any",output[t.search("any")]))
    # print("{} ---- {}".format("a", output[t.search('a')]))
    # print(t.hasAChild())
    # print(t.printKeys())



#  Trie with sets or dicts

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd

    
    def startWithPrefix(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


    def delete(self, word):
        def recursive(node, word, i):
            if i == len(word):
                if not node.isEnd:
                    return False
                node.isEnd = False
                return len(node.children) == 0

            if word[i] not in node.children:
                return False
            need_delete = recursive(node.children[word[i]], word, i+1)
            if need_delete:
                node.children.pop(word[i])
                return len(node.children) == 0
            return False

    def printKeys(self):
        res = list()
        self.printAllKeys(self.root, res)


    def printAllKeys(self, root, res):
        if root.isEnd == True:
            print(''.join(res))
        for i in self.root.children:
            if root.children[i] is not None:
                ch = i
                res.append(ch)
                self.printAllKeys(root.children[i], res)
                res.pop()


if __name__ == '__main__':
    keys = ['arsh', 'ergon', 'the', 'many', 'okay']
    t = Trie()
    for key in keys:
        t.insert(key)
    
    print(t.search('arsh'))
    print(t.delete('arsh'))
    print(t.startWithPrefix('a'))
    print(t.search('arsh'))
    print(t.printKeys())
