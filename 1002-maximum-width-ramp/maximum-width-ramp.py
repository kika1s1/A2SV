class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = [i for i in range(n)]
        indices.sort(key=lambda i: (nums[i], i))
        print(indices)
        min_index = n  
        max_width = 0
        for i in indices:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)
        return max_width