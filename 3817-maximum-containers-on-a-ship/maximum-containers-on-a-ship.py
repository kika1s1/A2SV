class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        l, r = 0, n*n
        best = 0
        while l <=r:
            mid = (l+r)//2
            if mid * w <= maxWeight:
                best = mid
                l = mid +1
            else:
                r = mid-1
        return best 