class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        b = 0
        ld = []
        n = len(heights)

        for i in range(n - 1):
            if heights[i] < heights[i + 1]:
                d = heights[i + 1] - heights[i]
                if len(ld) < ladders:
                    heapq.heappush(ld, d)
                else:
                    b += heapq.heappushpop(ld, d)

                if b > bricks:
                    return i

        return n - 1