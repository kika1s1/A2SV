class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            row = matrix[i]
            l, r = 0, len(row)-1
            while l <= r:
                row[l], row[r] = row[r], row[l]
                r -=1
                l +=1
        