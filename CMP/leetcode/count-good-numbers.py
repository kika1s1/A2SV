class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5,(n + 1)//2,(1000000007))*pow(4,n//2,1000000007))%1000000007