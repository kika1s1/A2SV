class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # if n == 0:
        #     return False
        # while n >= 1:
        #     if n == 1:
        #         return True
        #     n /= 2
        # return False
        return n > 0 and (n & (n - 1)) == 0
