class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(index, curr, k):
            if len(curr) == k:
                ans.append(curr[:])
                return  
            for i in range(index, n+1):
                curr.append(i)
                backtrack(i + 1, curr, k)
                curr.pop()
            return ans
        return backtrack(1, [], k)
        