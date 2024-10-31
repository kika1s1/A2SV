class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        p1 = self.find(u)  
        p2 = self.find(v)  

        if p1 == p2:
            return True, [u, v]  
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1

        return False, []



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        un = UnionFind(len(edges))
        for i in range(len(edges)):
            is_cycle,edge = un.union(edges[i][0],  edges[i][1])
            if is_cycle:
                return edge
        return []