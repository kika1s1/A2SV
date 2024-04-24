class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        cnt = 0
        total = 0
        happiness.sort()
        for i in range(k):
            val = happiness.pop() - cnt
            cnt +=1
            total +=val if val > 0 else 0
        return total