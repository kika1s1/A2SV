class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        def backtrack(curr):
            if len(curr) == len(nums[0]):
                if "".join(curr) not in nums:
                    return ans.append("".join(curr))
                return False, []

            curr.append("0")
            backtrack(curr)
            curr.pop()
            curr.append("1")
            backtrack(curr)
            curr.pop()
                
        backtrack([])
        return ans[0]