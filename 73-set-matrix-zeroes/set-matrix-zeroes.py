class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l_c = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    l_c.append(j)

        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for ii in range(len(matrix[i])):
                    matrix[i][ii] = 0
            else:
                for _ in l_c:
                    matrix[i][_] = 0
        return matrix

