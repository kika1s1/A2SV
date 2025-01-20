class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        col_count = defaultdict(int)
        row_count = defaultdict(int)
        position = defaultdict(int)
        for i in range(row):
            for j in range(col):
                position[mat[i][j]] = (i, j)
        for index, num in enumerate(arr):
            x, y = position[num]
            row_count[x]+= 1
            col_count[y]+= 1
            if row_count[x] >=col or col_count[y]>= row:
                return index