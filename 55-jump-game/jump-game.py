class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if (nums[i] + i ) >=start:
                start = i
        return True if start == 0 else False