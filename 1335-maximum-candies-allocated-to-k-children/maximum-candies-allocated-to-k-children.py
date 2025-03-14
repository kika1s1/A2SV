class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(candies, mid):
            cnt = 0
            for cand in candies:
                cnt +=(cand // mid)
            return cnt >=k
        l, r = 1, max(candies)
        best = 0
        while l <=r:
            mid = (l+r)//2
            if possible(candies, mid):
                best = mid
                l = mid+1
            else:
                r = mid-1
        return best
            