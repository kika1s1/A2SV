class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        l=0
        removes=0
        for r in range(n):
            if (colors[r]!=colors[l]):
                sameColors=neededTime[l:r]
                removes+=sum(sameColors)-max(sameColors)
                l=r
        removes+=sum(neededTime[l:])-max(neededTime[l:])
        return removes
        