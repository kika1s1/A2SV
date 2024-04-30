class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        b = n  

        for i in range(n):
            b ^= i ^ nums[i]

        return b