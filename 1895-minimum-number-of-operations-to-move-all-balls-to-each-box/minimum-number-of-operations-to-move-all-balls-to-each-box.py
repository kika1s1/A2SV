class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]* len(boxes)
        lcount , rcount , lcost , rcost  , n = 0 ,0,0,0,len(boxes)
        for i in range(1, n):
            if boxes[i-1] == '1':
                lcount += 1
            lcost += lcount
            ans[i] = lcost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                rcount += 1
            rcost += rcount
            ans[i] += rcost
        return ans
        