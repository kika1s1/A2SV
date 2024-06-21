from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        tot = 0
        maxim = 0
        n = len(customers)
        
        for i in range(minutes):
            if grumpy[i] == 1:
                tot += customers[i]
        maxim = tot
        
        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                tot -= customers[i - minutes]
            if grumpy[i] == 1:
                tot += customers[i]
            maxim = max(maxim, tot)
        
        satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]
        
        return maxim + satisfied
