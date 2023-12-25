class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0,0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l +=1
            r +=1
        return  True if l == len(s) else False
            