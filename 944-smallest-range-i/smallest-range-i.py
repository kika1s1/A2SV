class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        mn = min(nums)+k
        ans = (mx - mn - k) if mx - mn >= k else 0
        return ans