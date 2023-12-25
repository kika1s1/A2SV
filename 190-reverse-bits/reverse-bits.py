class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, 'b').zfill(32)[::-1], 2)