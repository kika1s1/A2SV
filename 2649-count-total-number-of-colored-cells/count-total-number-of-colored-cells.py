class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        addition = 0
        for i in range(2, n+1):
            addition +=4
            ans +=addition
        return ans
