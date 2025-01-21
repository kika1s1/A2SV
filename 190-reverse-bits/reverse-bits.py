class Solution:
    def reverseBits(self, n: int) -> int:
        ans = []
        for i in range(32):
            last = n&1
            ans.append(str(last))
            n >>=1
        return int("".join(ans),2)