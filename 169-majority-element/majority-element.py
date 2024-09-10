class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                ans = num
            cnt += (1 if num == ans else -1)
        return ans