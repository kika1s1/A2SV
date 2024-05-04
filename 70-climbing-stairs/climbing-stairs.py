class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, memo):
            if n <= 3:
                return n
            if n not in memo:
                memo[n] = dp(n-1, memo) + dp(n-2, memo)
            return memo[n]
        memo = {}
        return dp(n, memo)