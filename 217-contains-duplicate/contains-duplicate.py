class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        valRep = Counter(nums)
        for i in valRep.values():
            if i >=2:
                return True
        return False