class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c))+1):
            b = sqrt(c-i*i)
            if b == int(b):
                return True
        return False