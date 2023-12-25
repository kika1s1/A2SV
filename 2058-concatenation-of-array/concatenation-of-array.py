class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        total = len(nums)
        for i in range(total):
            nums.append(nums[i])
        return nums