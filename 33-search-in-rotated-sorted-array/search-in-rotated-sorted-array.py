class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target < nums[m]:
                l, r = (l, m - 1) if target >= nums[l] or nums[l] > nums[m] else (m + 1, r)
            elif target > nums[m]:
                l, r = (m + 1, r) if target <= nums[r] or nums[r] < nums[m] else (l, m - 1)
            else: return m
        
        return -1
