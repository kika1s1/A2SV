class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    cnt +=1
        return cnt