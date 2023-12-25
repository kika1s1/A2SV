class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            product *=i
        if product >= 1:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
        