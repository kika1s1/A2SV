# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 1
#         for i in range(n-1):
#             temp = one
#             one = one + two
#             two = temp
#         return one 

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def f(n):
            if n<=2: return n
            return f(n-1)+f(n-2)
        return f(n)
        