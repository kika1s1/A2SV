class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def checkPerimeter(grid, r, c, ROWS, COLS):
            if grid[r][c] == 0:
                return 0
           
            cnt_direction = 4
            if c < COLS-1:
                if grid[r][c+1] == 1:
                    cnt_direction -=1
            if r>0 and ROWS > r:
                if grid[r-1][c] == 1:
                    cnt_direction -=1
            if c > 0 and COLS > c:
                if grid[r][c-1] == 1:
                    cnt_direction -=1
            if r < ROWS-1:
                if grid[r+1][c] == 1:
                    cnt_direction -=1
            return cnt_direction




        cnt = 0
        ROWS, COLS = len(grid), len(grid[0])
        for c in range(COLS):
            for r in range(ROWS):
                cnt += (checkPerimeter(grid, r, c, ROWS, COLS))
        return cnt