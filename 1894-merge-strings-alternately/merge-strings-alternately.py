class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        n, m = len(word1), len(word2)
        i, j = 0, 0
        while i < n and j < m:
            ans +=word1[i]
            ans +=word2[j]
            i +=1
            j +=1
        while i < n:
            ans +=word1[i]
            i +=1
        while j < m:
            ans +=word2[j]
            j +=1
        return ans