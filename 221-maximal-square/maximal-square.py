class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            
            if matrix[r][c] == "1":
                right = dfs(r, c+1)
                bottom = dfs(r+1, c)
                diag = dfs(r+1, c+1)
                memo[r][c] = 1 + min(right, bottom, diag)
            else:
                memo[r][c] = 0
            
            return memo[r][c]
        
        max_side = 0
        for i in range(rows):
            for j in range(cols):
                max_side = max(max_side, dfs(i, j))
        
        return max_side * max_side