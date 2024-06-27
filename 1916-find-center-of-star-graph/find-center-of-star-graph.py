class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ans = set(edges[0])
        for edge in edges:
            ans &=set(edge)
        for i in ans:
            return i