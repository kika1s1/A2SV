class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                current_sum = nums[i]+nums[start]+nums[end]
                if current_sum > target:
                    end -= 1
                else:
                    start += 1
                if abs(current_sum - target) < abs(res - target):
                    res = current_sum
        return res