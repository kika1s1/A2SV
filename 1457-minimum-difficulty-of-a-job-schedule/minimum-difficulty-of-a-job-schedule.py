class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        
        dp = [[float('inf') for _ in range(n)] for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        
        dp[0] = [max(jobDifficulty[:i+1]) for i in range(n)]
        
        for day in range(1, d):
            for i in range(day, n):
                if day == i:
                    dp[day][i] = sum(jobDifficulty[:i+1])
                    continue
                for j in range(day-1, i):
                    dp[day][i] = min(dp[day][i], dp[day-1][j] + max(jobDifficulty[j+1:i+1]))
            
        return dp[d-1][n-1]