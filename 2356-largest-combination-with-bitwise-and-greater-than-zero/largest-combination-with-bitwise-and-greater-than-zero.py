class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0]*30
        for c  in candidates:
            for i in range(30):
                if (c & (1<<i)>0):
                    count[i] +=1
        return max(count)