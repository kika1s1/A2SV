class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxim = 0
        visited = set()
        for num in nums:
            if num in visited:
                continue
            cnt = 0
            while num in nums:
                visited.add(num)
                cnt +=1
                num +=1
            maxim = max(maxim, cnt)
        return maxim
