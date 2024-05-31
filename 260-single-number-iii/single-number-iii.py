class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] not in hashTable:
                hashTable[nums[i]] = 1
            else:
                del hashTable[nums[i]]
        return list(hashTable.keys())
