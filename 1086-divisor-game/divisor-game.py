class Solution:
    def divisorGame(self, n: int) -> bool:
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            for i in range(1, n // 2 + 1):
                if n % i == 0 and not dp(n - i):
                    # memo[n] = True
                    return True
            memo[n] = False
            return False
        return dp(n)