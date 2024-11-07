class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_count = [0] * 24
        for i in range(24):
            for num in candidates:
                # Check if the i-th bit is set.
                if (num & (1 << i)) != 0:
                    bit_count[i] += 1

        return max(bit_count)