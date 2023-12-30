class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+2, len(nums)+1):
        #         sub = nums[i:j]
        #         if sum(sub) % k == 0:
        #             return True
        # return False

        reminder = {0:-1}
        # if the first index is divisible pass
        total = 0
        for i, n in enumerate(nums):
            total +=n
            r = total%k
            if r not in reminder:
                reminder[r] = i
            elif i - reminder[r] >1:
                return True
        return False
