class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n
        while(l<=r):
            mid = (l+r)//2
            count = 0 
            for i in nums:
                if(i>=mid):
                    count +=1

            if (count == mid):
                return mid
            elif count > mid:
                l = mid + 1
            else : 
                r = mid - 1

        return -1            


