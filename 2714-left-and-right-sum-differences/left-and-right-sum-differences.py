class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[]
        rightsum=[]
        res=[0]*len(nums)
        sum1=0
        for i in range(len(nums)):
            if i==0:
                leftsum.append(0)
            else:
                sum1=nums[i-1]+sum1
                leftsum.append(sum1)
        for j in range(len(nums)):
            if j==len(nums)-1:
                rightsum.append(0)
            else:
                sum2=0
                x=sum(nums[j+1:])
                rightsum.append(x)
        for k in range(len(nums)):
            res[k]=abs(leftsum[k]-rightsum[k])
        return res