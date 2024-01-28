from collections import Counter

class Solution:
    def mostFrequentEven(self, nums) -> int:
        #tamirat
        counter = Counter([i for i in nums if i % 2 == 0])
        if not counter:
            return -1
        res = {x: count for x, count in counter.items() if count == max(counter.values())}
        return min(res.keys())