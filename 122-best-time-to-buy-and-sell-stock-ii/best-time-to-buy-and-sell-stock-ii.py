class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(-1)
        left = 0
        ans = 0
        for i in range(1,len(prices)):
            if prices[i-1] > prices[i]:
                ans +=(prices[i-1] - prices[left])
                left =  i
        return ans
            
