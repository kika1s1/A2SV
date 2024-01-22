class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        ans = set()
        while nums:
            mn = min(nums)
            nums.remove(mn)
            mx = max(nums)
            nums.remove(mx)
            ans.add((mn+mx)/2)
        return len(ans)