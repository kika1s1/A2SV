class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minim = float("inf")
        for i in range(len(prices)):
            if minim > prices[i]:
                minim = prices[i]
            else:
                ans  +=(prices[i] - minim)
                minim = prices[i]
        return ans
            
