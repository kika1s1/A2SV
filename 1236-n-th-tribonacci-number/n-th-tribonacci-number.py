class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n ==0:
            return 0
        if n <= 2:
            return 1
        for i in range(3, n+1):
            new = a+b+c
            a, b, c = b, c,new
        return c

        