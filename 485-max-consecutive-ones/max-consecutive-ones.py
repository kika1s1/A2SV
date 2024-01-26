class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxim = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt +=1
                maxim = max(maxim, cnt)
            else:
                cnt = 0
        return maxim