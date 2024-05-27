class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pos = set(nums)
        for i in range(max(nums)+2):
            if i not in pos:
                return i

