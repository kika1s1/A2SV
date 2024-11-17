class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        results = []
        R, C = len(grid), len(grid[0])
        prev = grid[0][0]
        for i in range(R):
            for j in range(C):
                if abs(prev - grid[i][j]) % x !=0:
                    return -1
                else:
                    results.append(grid[i][j])
        results.sort()
        mid = len(results)//2
        value = results[mid]
        cnt = 0
        for num in results:
            if num == value:
                continue
            else:
                times = abs(num - value) //x
                cnt +=times
        return cnt

