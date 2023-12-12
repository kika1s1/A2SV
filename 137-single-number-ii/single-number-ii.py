class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictRep = Counter(nums)
        for i, value in dictRep.items():
            if value == 1:
                return i