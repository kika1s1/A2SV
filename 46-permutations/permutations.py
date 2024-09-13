class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cand):
            if len(cand) == len(nums):
                ans.append(cand[:])
            for num in nums:
                if num in cand:
                    continue
                cand.append(num)
                backtrack(cand)
                cand.pop()
        backtrack([])
        return ans