class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = str(x)
        t = 0
        for i in s:
            t +=int(i)
        if x%t == 0:
            return t
        return -1
