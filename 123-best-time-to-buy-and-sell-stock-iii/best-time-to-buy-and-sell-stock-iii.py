class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy, first_sell = -prices[0], 0
        second_buy, second_sell = -prices[0], 0
        for price in prices[1:]:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)
        return second_sell