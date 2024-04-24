# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         heap = []
#         for i in range(1,n+1):
#             heappush(heap, str(i))
#         ans = []
#         while heap:
#             ans.append(int(heappop(heap)))
#         return ans


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        
        def recursive(value):
            if len(ans) >= n:
                return
            ans.append(value)
            if (value * 10) <= n:
                recursive(value * 10)
            if value + 1 <= n and int(str(value)[-1]) < 9:
                recursive(value + 1)
        recursive(1)

        return ans