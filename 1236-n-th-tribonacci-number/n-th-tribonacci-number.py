
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        l = [0, 1, 1]
        for i in range(n-2):
            a, b, c = l[-1], l[-2], l[-3]
            l.append(a+b+c)
        return l[-1]
