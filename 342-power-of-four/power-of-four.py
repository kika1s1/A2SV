class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n.bit_count() == 1 and int('10' * 16, 2) & n == 0