class Solution:
    def dfs(self, graph: List[List[int]], visited: List[bool], source: int):
        visited[source] = True
        for child in graph[source]:
            if visited[child] == False:
                self.dfs(graph, visited, child)

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for arr in edges:
            graph[arr[0]].append(arr[1])
            graph[arr[1]].append(arr[0])
            
        visited = [False] * n
        self.dfs(graph, visited, source)
        return visited[destination]