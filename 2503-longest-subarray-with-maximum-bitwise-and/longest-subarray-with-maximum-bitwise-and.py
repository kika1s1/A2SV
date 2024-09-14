class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxim = 0
        ans = 0
        length = 0
        for num in nums:
            if num > maxim:
                maxim = num
                length  = 1
                ans = length
            elif num == maxim:
                length +=1
                ans = max(ans, length)
            else:
                ans = max(ans, length)
                length = 0
        return ans

