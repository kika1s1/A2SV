class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            check = target - j
            if check in nums and nums.index(check) != i:
                return [i, nums.index(check)]