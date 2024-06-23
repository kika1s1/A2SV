class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        r = len(nums)-1
        while r >= 0:

            if nums[r] == 9:
                nums[r] = 0
                r -=1
            else:
                nums[r] +=1
                return nums
        nums.insert(0, 1)
        return nums
            