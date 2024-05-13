class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        COLS, ROWS = len(grid[0]), len(grid)
        for i in range(ROWS):
            for k in range(COLS):
                grid[i][k] = str(grid[i][k])
            if grid[i][0] == "0":
                for j in range(COLS):
                    grid[i][j] = "1" if grid[i][j] == "0" else "0"
        cols_change = set()
        for i in range(COLS):
            cnt = 0
            for j in range(ROWS):
                if grid[j][i] =="0":
                    cnt +=1
            if ROWS-cnt < cnt:
                cols_change.add(i)
        for i in range(ROWS):
            for j in range(COLS):
                if j in cols_change:
                    grid[i][j] = "1" if grid[i][j] == "0" else "0"
        
        total = 0
        for row in grid:
            total +=int("".join(row), 2)

        return total


                    

            
                

