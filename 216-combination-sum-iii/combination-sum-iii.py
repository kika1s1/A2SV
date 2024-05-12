class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        checked = []
        def backtrack(curr):
            if len(curr) ==k and sum(curr) == n and set(curr) not in checked:
                checked.append(set(curr))
                ans.append(curr[:])
            if len(curr) > k or sum(curr) > n:
                return 
            for i in range(1, 10):
                if  i in curr:
                    continue
                curr.append(i)
                backtrack(curr)
                curr.pop()
        backtrack([])
        return ans