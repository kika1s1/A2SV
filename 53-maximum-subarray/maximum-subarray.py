class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = float("-inf")
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total < 0:
                maxim = max(maxim, total)
                total = 0
            else:
                maxim = max(maxim,total)
        return maxim



        return 0
            
            