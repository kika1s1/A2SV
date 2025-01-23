class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        communicate = defaultdict(set)
        R, C = len(grid), len(grid[0])
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    got = False
                    # horizontal
                    for left in range(C):
                        if (i, left) !=(i, j) and grid[i][left] ==1:
                            got = True
                            print((i, left),(i, j) )
                            break

                    # vertical
                    for down in range(R):
                        if (down, j) !=(i, j) and grid[down][j] ==1:
                            got = True
                            break
                    if got:
                        ans +=1
        return ans