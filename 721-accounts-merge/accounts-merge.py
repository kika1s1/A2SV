from typing import *
from collections import defaultdict
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)] 
        self.rank = [i for i in range(size)]
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
        
    
    def union(self, x, y):
        rooty = self.find(y)
        rootx = self.find(x)
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
        elif self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        else:
            self.parent[rootx] = rooty
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                acc1 = set(accounts[i][1:])
                acc2 = set(accounts[j][1:])
                for email in acc1:
                    if email in acc2:
                        uf.union(i, j)
        res = defaultdict(set)
        for i in range(n):
             parent = uf.find(i)
             for email in accounts[i][1:]:
                res[parent].add(email)
        ans = []
        for id, emails in res.items():
            ans.append([accounts[id][0]] + sorted(emails))
        return ans