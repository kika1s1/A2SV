class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {x:set() for x in range(1, n+1)}
        for a, b in trust:
            graph[a].add(b)
        ans = -1
        candidates = []
        for key, value in graph.items():
            if not  value:
                candidates.append(key)
        for person in candidates:
            isTrue = True
            for key, value in graph.items():
                if key != person and person not in value:
                    isTrue = False
                    break
            if isTrue:
                return person
        return -1

                
