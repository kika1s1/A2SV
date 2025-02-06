class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        rep=Counter()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                rep[nums[i]*nums[j]]+=1
        ans=0
        for value in rep.values():
            ans +=(value*(value-1)*4)
        return ans 
            