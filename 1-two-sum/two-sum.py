class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, j in enumerate(nums):
            if j in hashMap:
                return [hashMap[j], i]
            else:
                hashMap[target-j] = i
