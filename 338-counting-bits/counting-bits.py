class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            t = 0
            for j in bin(i)[2:]:
                t +=int(j)
            ans.append(t)
            t = 0
        return ans