class Solution:
    def rob(self, nums: List[int]) -> int:
        prevprev = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            prev, prevprev = max(prevprev + nums[i], prev), prev
        return prev
        