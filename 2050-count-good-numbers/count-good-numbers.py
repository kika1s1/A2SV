class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        five = (n + 1) // 2
        four = n // 2
        
        return (pow(5, five, MOD) * pow(4, four, MOD)) % MOD
