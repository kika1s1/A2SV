class Solution:
    def reverseBits(self, n: int) -> int:
        ans = []
        for bit in bin(n)[2:][::-1]:
            ans.append(bit)
        for i in range(32-len(ans)):
            ans.append("0")
        return int("".join(ans), 2)