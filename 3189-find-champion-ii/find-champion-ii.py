from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            if n == 1:
                return 0
            else:
                return -1
        
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
        
        def dfs(graph, visited, node):
            visited.add(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    dfs(graph, visited, neighbour)
        
        for u, v in edges:
            visited = set()
            dfs(graph, visited, u)
            if len(visited) == n:
                return u
        
        return -1