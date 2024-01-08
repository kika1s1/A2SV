class Solution:
    def fib(self, n: int) -> int:
        dp = [0 for x in range(n+1)]
        for i in range(1, n+1):
            dp[0], dp[1] = 0, 1
            if i >= 2:
                dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
