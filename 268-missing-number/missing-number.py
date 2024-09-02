class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        N = len(nums)+1
        for i in range(N):
            if i not in nums:
                return i
        return N