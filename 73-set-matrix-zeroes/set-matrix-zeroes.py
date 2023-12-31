class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        M, N = len(matrix), len(matrix[0])
        removed_row_idxes, removed_col_idxes = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    continue

                if i not in removed_row_idxes:
                    removed_row_idxes.append(i)
                
                if j not in removed_col_idxes:
                    removed_col_idxes.append(j)
        for r in removed_row_idxes:
            for k in range(len(matrix[r])):
                matrix[r][k] = 0

        for c in removed_col_idxes:
            for k in range(len(matrix)):
                matrix[k][c] = 0    
        return matrix