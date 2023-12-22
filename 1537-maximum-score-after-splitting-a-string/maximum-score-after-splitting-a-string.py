class Solution:
    def maxScore(self, s: str) -> int:
        curr0, curr1, total1 = 0, 0, 0

        for c in s:
            if c == '1':
                total1 += 1
        
        res = 0
        for c in s[:-1]:
            if c == '0':
                curr0 += 1
            else:
                curr1 += 1
            res = max(res, curr0 + total1-curr1)
        return res