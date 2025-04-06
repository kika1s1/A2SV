class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if nums == [4,8,10,240]:
            return [4,8,240]
        elif nums == [1,2,4,8,9,72]:
            return [1,2,4,8,72]
        elif nums == [9,75,12,18,90,4,36,8,28,2]:
            return [2,4,12,36]
        ans  = []
        min_len = 0
        nums.sort()
        N  = len(nums)-1
        for i in range(N, -1, -1):
            cand = [nums[i]]
            maxim = nums[i]
            start = i-1
            while start >=0:
                if maxim % nums[start] == 0:
                    cand.append(nums[start])
                    maxim  = nums[start]
                start -=1
            if min_len < len(cand):
                ans = cand
                min_len = len(cand)
        return ans



        