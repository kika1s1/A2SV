class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        maxim = float("-inf")
        for i in nums:
            if i < 0:
                if -1*i in seen:
                    maxim = max(abs(i), maxim)
                seen.add(i)
            else:
                if -1*i in seen:
                    maxim = max(abs(i), maxim)
                seen.add(i)
        if maxim ==float("-inf"):
            return -1
        else:
            return maxim