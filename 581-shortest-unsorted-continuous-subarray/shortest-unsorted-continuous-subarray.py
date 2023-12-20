class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        l, r = 0, len(nums)
        totalLength = len(nums)
        if len(nums) == 1:
            return 0
        while l < r:
            sub = nums[l:r]
            if (min(sub) != nums[l]) and (max(sub) != nums[r-1]):
                break
            if min(sub) == nums[l]:
                l += 1
                if totalLength == 0:
                    break
                totalLength -= 1
            if max(sub) == nums[r-1]:
                r -= 1
                if totalLength == 0:
                    break
                totalLength -= 1
        return totalLength