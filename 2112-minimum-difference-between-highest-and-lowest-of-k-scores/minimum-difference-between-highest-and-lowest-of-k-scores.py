class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k-1
        ans =float("inf")
        while r < len(nums):
            ans = min(ans, (nums[r]-nums[l]))
            l, r = l +1, r +1
        return ans

        