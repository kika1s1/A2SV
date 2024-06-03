class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxim  = float("-inf")
        cnt = 0
        for i in range(len(nums)):
            if i == 0:
                cnt +=nums[i]
            else:
                if nums[i-1] < nums[i]:
                    cnt +=nums[i]
                    
                else:
                    cnt = nums[i]
            maxim = max(cnt, maxim)
        return maxim

