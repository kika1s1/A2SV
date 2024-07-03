class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 3:
            return 0
            
        nums.sort()
        ans = float('inf')
        
        ans = min(ans, nums[-1] - nums[3])

        ans = min(ans, nums[-4] - nums[0])

        ans = min(ans, nums[-2] - nums[2])

        ans = min(ans, nums[-3] - nums[1])
        return ans