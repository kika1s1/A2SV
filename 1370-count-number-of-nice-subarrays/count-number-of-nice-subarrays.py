class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        helper = [-1] + [i for i, el in enumerate(nums) if el % 2] + [len(nums)]

        for i in range(1, len(helper) - k):
            ans += (helper[i] - helper[i - 1]) * (helper[i + k] - helper[i + k - 1])

        return ans