class Solution:
    def furthestBuilding(
        self, heights: List[int], bricks: int, ladders: int
    ) -> int:
        jumps = []
        for i, (h0, h1) in enumerate(pairwise(heights)):
            if (d := h1 - h0) > 0:
                heapq.heappush(jumps, d)
            if len(jumps) > ladders:
                bricks -= heapq.heappop(jumps)
            if bricks < 0:
                return i
        return len(heights) - 1