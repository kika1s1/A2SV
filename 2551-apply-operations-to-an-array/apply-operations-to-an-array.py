class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l, r = 0, 1
        while l < r < len(nums):
            if nums[l] == nums[r]:
                nums[l] = 2*nums[l]
                nums[r] =0
                r +=2
                l +=2
            else:
                r +=1
                l +=1
            
        l, r = 0, 1
        while l < r < len(nums):
            if nums[l] == 0 and nums[r] !=0:
                nums[l], nums[r] = nums[r], nums[l]
            elif nums[l] == 0 and nums[r] == 0:
                r +=1

            else:
                r +=1
                l +=1
        return nums