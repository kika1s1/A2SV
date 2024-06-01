class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(len(s)):
            sub = s[:i]
            cnt = s.count(sub)
            s_l = len(sub)
            if cnt * s_l == l:
                return True
        return False