class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        mx = max(nums)
        current = nums[0]
        length = 0
        res = 0
        for n in nums:
            current &= n
            length += 1

            if current != mx:
                length = 1
                current = n

            if current == mx:

                res = max(res, length)

        return res

        