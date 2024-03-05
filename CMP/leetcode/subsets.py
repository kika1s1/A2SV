class Solution:
    def subsets(self, s: List[int]) -> List[List[int]]:
        ans = []
        n = len(s)
        for r in range(n + 1):
            for subset in combinations(s, r):
                ans.append(list(subset))
        return ans
