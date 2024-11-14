class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res  = 1
        for i in range(len(points)):
            p1 = points[i]
            count = defaultdict(int)
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:
                    slope = float("inf")
                else:
                    slope  = (p2[1]-p1[1])/(p2[0] - p1[0])
                count[slope] +=1
                res = max(res, count[slope]+1)
        return res