class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        existed = set(arr)
        cnt = 0
        for i in range(1, arr[-1]+1):
            if i not in existed:
                print(i)
                cnt +=1
                if cnt == k:
                    return i
        return (k-cnt)+arr[-1]