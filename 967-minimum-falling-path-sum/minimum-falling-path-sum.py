class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return matrix[0][0]
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp = matrix.copy() 
        for i in range(n - 2, -1, -1):
            for j in range(n):
                min_path = dp[i + 1][j]
                if j > 0:
                    min_path = min(min_path, dp[i + 1][j - 1])
                if j < n - 1:
                    min_path = min(min_path, dp[i + 1][j + 1])
                dp[i][j] += min_path

        result = float('inf')
        for num in dp[0]:
            result = min(result, num)
        return result