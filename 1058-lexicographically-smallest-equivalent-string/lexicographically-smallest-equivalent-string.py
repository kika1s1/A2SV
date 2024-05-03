class Disjoint:
    def __init__(self,n):
        self.size=[1]*n
        self.parent=[i for i in range(n)]

    def findUPar(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findUPar(self.parent[node])
        return self.parent[node]

    def union(self,u,v):
        ulp_u=self.findUPar(u)
        ulp_v=self.findUPar(v)
        if ulp_u==ulp_v:
            return
        if ulp_u<ulp_v:
            self.parent[ulp_v]=ulp_u
        elif ulp_u>ulp_v:
            self.parent[ulp_u]=ulp_v
            

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        disjoint=Disjoint(26)
        n=len(s1)
        for i in range(n):
            # print(s1[i],s2[i],ord(s1[i])-97,ord(s2[i])-97)
            disjoint.union(ord(s1[i])-97,ord(s2[i])-97)
        
        st=""
        for i in range(26):
            disjoint.findUPar(i)
        # print(disjoint.parent)

        for i in baseStr:
            x=disjoint.findUPar(ord(i)-97)
            st+=chr(x+97)
        return st