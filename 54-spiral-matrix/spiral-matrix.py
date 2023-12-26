class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        xmin = -1
        xmax = len(matrix)
        ymin = -1
        ymax = len(matrix[0])
        x = y = 0
        res = [matrix[0][0]]

        while xmin <= xmax and ymin <= ymax:
            for i, direction in enumerate([[0,1],[1,0],[0,-1],[-1,0]]):
                while xmin < x + direction[0] < xmax and ymin < y + direction[1] < ymax:
                    x += direction[0]
                    y += direction[1]
                    res.append(matrix[x][y])
                if i == 0:
                    xmin += 1
                elif i == 1:
                    ymax -= 1
                elif i == 2:
                    xmax -= 1
                elif i == 3:
                    ymin += 1
                if xmin + 1 == xmax or ymin + 1 == ymax:
                    break
        return res