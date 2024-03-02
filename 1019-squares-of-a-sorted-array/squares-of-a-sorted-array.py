class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        
        for i in nums:
            insort(out, i*i)
        
        return out