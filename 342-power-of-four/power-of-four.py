class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        return n>0 and log(n,4).is_integer()    