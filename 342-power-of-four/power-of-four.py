class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if int(n) != n:
            return False
        if n == 1:
            return True
        if n < 1:
            return False
        return self.isPowerOfFour(n/4)