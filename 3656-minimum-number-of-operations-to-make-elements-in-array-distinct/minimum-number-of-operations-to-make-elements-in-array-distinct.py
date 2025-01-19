class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        visited = set()
        n = len(nums)
        for i in range(1,len(nums)+1):
            if nums[-i] not in visited:
                visited.add(nums[-i])
            else:
                times = ceil((len(nums)+1-i)/3)
                return times
        return 0