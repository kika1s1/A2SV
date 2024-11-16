class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = [1] * n
        remaining = k - n
        i = 0
        while remaining >= 25:
            s[i] += 25
            remaining -= 25
            i += 1
        if remaining >= 1:
            s[i] += remaining
        return(''.join(list(map(lambda x: chr(ord('a') + x - 1), s[::-1]))))