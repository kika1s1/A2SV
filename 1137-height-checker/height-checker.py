class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        secondVal = heights.copy()
        secondVal.sort()
        cnt = 0
        for i in range(len(secondVal)):
            if secondVal[i] != heights[i]:
                cnt +=1
        return cnt