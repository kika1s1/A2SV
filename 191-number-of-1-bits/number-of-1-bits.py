class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(str(bin(n)).replace("0","").replace("b",""))