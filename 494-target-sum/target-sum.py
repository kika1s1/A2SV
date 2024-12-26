class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        memo = {}
        def backtrack(index, curr_sum):
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            
            if index == N:
                if curr_sum == target:
                    return 1
                else:
                    return 0
            
            pos = backtrack(index + 1, curr_sum + nums[index])
            neg = backtrack(index + 1, curr_sum - nums[index])
            memo[(index, curr_sum)] = pos + neg
            return memo[(index, curr_sum)]
        return backtrack(0, 0)