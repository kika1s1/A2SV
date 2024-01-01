class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-1*k]
        min_val, max_val = min(nums), max(nums)
        count = [0] * (max_val - min_val + 1)

        for i in nums:
            count[i-min_val] += 1

        remain = k
        for num in range(len(count)-1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_val
        