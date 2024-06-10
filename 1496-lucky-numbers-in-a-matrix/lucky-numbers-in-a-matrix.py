from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        R, C = len(matrix), len(matrix[0])
        
        row_mins = [min(row) for row in matrix]
        
        col_maxs = [max(col) for col in zip(*matrix)]
        
        for i in range(R):
            for j in range(C):
                val = matrix[i][j]
                if val == row_mins[i] and val == col_maxs[j]:
                    ans.append(val)
                    
        return ans
