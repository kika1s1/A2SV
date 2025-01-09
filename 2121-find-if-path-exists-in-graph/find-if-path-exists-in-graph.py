class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)
        visited = set()
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        stack.append(neighbour)
        return False

            

        return False
        