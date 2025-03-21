class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        a, b = 0, 0
        n = len(costs)-1
        for i in range(len(costs)//2):
            a +=costs[i][0]
            b +=costs[n-i][1]
        return a + b