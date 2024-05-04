class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        i = 0 
        while n: 
            while x & 1<<i:
                i += 1
            if n & 1:
                x ^= 1 << i
            n >>= 1
            i += 1
        return x 