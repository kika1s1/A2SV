class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashIndex = {}
        for i, num in enumerate(nums):
            val = target - num
            hashIndex[val] = i
        ans = []
        for i, num in enumerate(nums):

            if num in hashIndex and i != hashIndex[num]:
                return sorted([hashIndex[num], i])
        return [-1, -1]