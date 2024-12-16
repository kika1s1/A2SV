class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))
        for i in range(k):
            num, index = heappop(heap)
            heappush(heap, (num*multiplier, index))
        ans = [0]*len(heap)
        for num, index in heap:
            ans[index] = num
        return ans