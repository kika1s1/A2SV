class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        trail = n//5
        while trail > 0:
            ans += trail
            trail //= 5
        return ans