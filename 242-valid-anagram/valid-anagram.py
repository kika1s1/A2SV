class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        isTrue = True
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in t:
                if s.count(s[i]) != t.count(s[i]):
                    isTrue = False
            else:
                isTrue = False
        return isTrue
