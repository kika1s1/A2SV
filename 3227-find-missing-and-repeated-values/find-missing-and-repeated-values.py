class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        rep_count = defaultdict(int)
        R, C  = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                rep_count[grid[i][j]] +=1
        miss = []
        double = []
        for i in range(1, R*C+1):
            if rep_count[i] ==0:
                miss.append(i)
            if rep_count[i] >=2:
                double.append(i)
        return double + miss