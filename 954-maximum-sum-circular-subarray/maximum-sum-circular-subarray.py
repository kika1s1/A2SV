class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax,gmin,cmax,cmin,total=nums[0],nums[0],0,0,0
        for n in nums:
            cmax=max(cmax+n,n)
            cmin=min(cmin+n,n)
            gmax=max(gmax,cmax)
            gmin=min(gmin,cmin)
            total+=n
        return max(gmax,total-gmin) if gmax>0 else gmax
  