class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(start, destination, visited):
            if start == destination:
                return True
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    if dfs(neighbor, destination, visited):
                        return True
            return False
        return dfs(source, destination, set())