class Trie:
    ALPHABET_SIZE = 26
    class TrieNode:
        def __init__(self):
            self.is_end = False
            self.children = [None] * Trie.ALPHABET_SIZE

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not curr.children[index]:
                curr.children[index] = self.TrieNode()
            curr = curr.children[index]
        curr.is_end = True

    def countChildren(self, node):
        count = 0
        for child in node.children:
            if child:
                count += 1
        return count

    def walkTrie(self, root):
        pCrawl = root
        prefix = ""
        while self.countChildren(pCrawl) == 1 and not pCrawl.is_end:
            for i, child in enumerate(pCrawl.children):
                if child:
                    prefix += chr(ord("a") + i)
                    pCrawl = child
                    break
        return prefix

    def commonPrefix(self, arr):
        for word in arr:
            self.insert(word)
        return self.walkTrie(self.root)

class Solution:
    def longestCommonPrefix(self, strs):
        trie = Trie()
        return trie.commonPrefix(strs)
