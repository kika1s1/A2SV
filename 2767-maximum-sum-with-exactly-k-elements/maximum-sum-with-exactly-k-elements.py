class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxim = max(nums)
        total = maxim
        for i in range(k-1):
            maxim +=1
            total +=maxim
        return total
