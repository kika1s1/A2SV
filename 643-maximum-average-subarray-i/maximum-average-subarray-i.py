class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) ==1:
            return nums[0]
        total = 0
        N = len(nums)
        ans = float("-inf")
        for i in range(N):
            if i < k:
                total +=nums[i]
            else:
                ans = max(ans, total/k)
                total +=nums[i]
                total -=nums[i-k]
        ans = max(ans, total/k)
        return ans
