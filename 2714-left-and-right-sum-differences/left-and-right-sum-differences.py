class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        answer = list()

        for i in range(len_nums):
            answer.append(abs(sum(nums[: i]) - sum(nums[i + 1 :])))
        
        return answer