class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def inbound(row, col):
            return (0 <= row and 0 <= col) and (row < len(grid) and col < len(grid[0]))
        ans = 0
        def dfs(row, col, is_parent = True):
            nonlocal ans, directions
            if not inbound(row, col):
                return
            if grid[row][col] == "0":
                return
            if is_parent:
                ans += 1
            grid[row][col] = "0"
            for x, y in directions:
                dfs(row+x, col+y, False)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
        return ans