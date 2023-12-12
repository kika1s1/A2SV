class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        num, i = set(nums), 1
        while i in num:
            i += 1
        return i
