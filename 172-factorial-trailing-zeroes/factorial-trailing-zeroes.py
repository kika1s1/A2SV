class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        t = int(n/5)
        while t > 0:
            ans += t
            t = int(t/5)
        return ans