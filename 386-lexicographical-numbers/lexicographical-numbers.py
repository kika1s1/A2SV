class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        heap = []
        for i in range(1,n+1):
            heappush(heap, str(i))
        ans = []
        while heap:
            ans.append(int(heappop(heap)))
        return ans