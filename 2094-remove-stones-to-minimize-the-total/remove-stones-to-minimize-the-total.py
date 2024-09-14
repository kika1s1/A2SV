class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for pile in piles:
            heappush(heap, -pile)
        for i in range(k):
            removed = heappop(heap)
            heappush(heap, (removed + (-(removed)//2)))
        return - (sum(heap))