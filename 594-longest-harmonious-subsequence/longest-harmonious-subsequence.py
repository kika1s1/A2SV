class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s=list(set(nums))
        sn=0
        for i in s:
            if i+1 in s:
                sn=max(sn,(nums.count(i)+nums.count(i+1)))
        return sn
        