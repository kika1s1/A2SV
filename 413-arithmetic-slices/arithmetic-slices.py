class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        count = 0

        for r in range(2, len(nums)):
            diff1 = nums[r] - nums[r-1]
            diff2 = nums[r-1] - nums[r-2]

            if diff1 == diff2:
                count += 1
            else:
                ans = count * (count + 1) // 2 + ans
                count = 0

        return count * (count + 1) // 2 + ans