
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(vertex, visited):
            if vertex == destination:
                return True
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            
            return False 
        return dfs(source, set())
