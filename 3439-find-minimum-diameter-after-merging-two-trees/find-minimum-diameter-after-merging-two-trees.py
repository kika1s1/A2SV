class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        d1 = self.treeDiameter(edges1)
        d2 = self.treeDiameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)

    def treeDiameter(self, edges: List[List[int]]) -> int:
        def dfs(i: int, fa: int, t: int):
            for j in g[i]:
                if j != fa:
                    dfs(j, i, t + 1)
            nonlocal ans, a
            if ans < t:
                ans = t
                a = i

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = a = 0
        dfs(0, -1, 0)
        dfs(a, -1, 0)
        return ans
        