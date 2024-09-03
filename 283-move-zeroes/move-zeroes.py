class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        N = len(nums)
        while r < N and l < r:
            if nums[l] == 0 and nums[r] !=0:
                nums[l],nums[r] = nums[r], nums[l]
                l +=1
                r +=1
            elif  nums[l] == 0 and nums[r] == 0:
                r +=1
            else:
                l +=1
                r +=1
        