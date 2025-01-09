class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[v].add(u)
            graph[u].add(v)
        for key in graph:
            is_centre = True
            for search in graph:
                if search !=key and  key not in graph[search]:
                    is_centre = False
                    break
            if is_centre:
                return key
