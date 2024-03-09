class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            for i in range(1,len(nums)):
                nums[i-1] = int(str(nums[i-1] + nums[i])[-1])
            nums.pop()
            # print(nums)
        return nums[0]



        