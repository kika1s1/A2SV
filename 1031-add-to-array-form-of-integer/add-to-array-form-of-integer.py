class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for ele in num:
            n = (n*10) + ele
        
        n = n+k
        
        num = []
        while n > 0:
            num.insert(0, n % 10)  
            n //= 10 
        return num