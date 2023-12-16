class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        isTrue = True
        if len(t) == len(s):
            for i in t:
                if s.count(i) != t.count(i):
                    isTrue = False
        else:
            return False
        return isTrue
            