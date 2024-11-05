class Solution:
    def minChanges(self, s: str) -> int:
        cnt = 0
        l, r = 0, 1
        while r < len(s):
            if s[l] !=s[r]:
                cnt +=1
            l +=2
            r +=2
        return cnt