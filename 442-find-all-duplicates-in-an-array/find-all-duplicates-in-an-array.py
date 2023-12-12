class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numRep = Counter(nums)
        ans = []
        for key, value in numRep.items():
            if value >1:
                ans.append(key)
        return ans