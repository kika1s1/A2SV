class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diff = start ^ goal
        return diff.bit_count()