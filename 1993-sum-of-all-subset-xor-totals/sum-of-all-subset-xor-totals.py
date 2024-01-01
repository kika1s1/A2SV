class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum |= i
            result = sum*(2**(len(nums)-1))
        return result