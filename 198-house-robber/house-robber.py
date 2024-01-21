class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        s0, s1 = [0, 0], [0, 0]
        s1[0] = nums[0]

        for i in range(1, n):
            s0[i % 2] = max(s0[(i - 1) % 2], s1[(i - 1) % 2])
            s1[i % 2] = s0[(i - 1) % 2] + nums[i]

        return max(s0[(n - 1) % 2], s1[(n - 1) % 2])

