class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} 
        def backtrack(curr_amount):
            if curr_amount in memo:
                return memo[curr_amount]
            if curr_amount == 0:
                return 0
            if curr_amount < 0:
                return float('inf')
            min_coins = float('inf')
            for coin in coins:
                result = backtrack(curr_amount - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)
            memo[curr_amount] = min_coins
            return min_coins
        min_coins = backtrack(amount)
        if min_coins == float('inf'):
            return -1
        else:
            return min_coins