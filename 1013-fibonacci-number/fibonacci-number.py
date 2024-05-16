class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        print(dp)
        return dp[n]
        