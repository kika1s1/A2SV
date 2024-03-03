class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.nSum(nums, target, 4, [], results)
        return results
    
    def nSum(self, nums: List[int], target: int, n: int, prefix: List[int], results: List[List[int]]):
        if len(nums) < n or nums[0] * n > target or nums[-1] * n < target:
            return
        
        if n == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    results.append(prefix + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(len(nums) - n + 1):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    self.nSum(nums[i + 1:], target - nums[i], n - 1, prefix + [nums[i]], results)