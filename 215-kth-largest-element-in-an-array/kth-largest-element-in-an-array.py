class Solution:
    def findKthLargest(self, nums: List[int], n: int) -> int:

        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        for _ in range(n-1):
            heapq.heappop(heap) 
        return -heapq.heappop(heap) 