class Solution:
    def integerBreak(self, n: int) -> int:
            # dp = [0] * (n + 1)
            # dp[1] = 1
            # dp[2] = 1
            # for i in range(3, n + 1):
            #     for j in range(1, i):
            #         dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
            # return dp[n]
            if n <=3:
                return n- 1
            d3 = n//3
            r3 = n % 3
            if r3 == 0:
                return 3**d3
            if r3 ==1:
                r3 = 4
                d3 -=1
            return r3 * (3**d3)
