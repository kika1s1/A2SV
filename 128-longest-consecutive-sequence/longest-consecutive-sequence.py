class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        longest = 0
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                cnt += 1
            else:

                cnt = 1
            longest = max(cnt, longest)
        return longest
