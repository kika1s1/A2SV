class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr)/2
        cntr = sorted(Counter(arr).items(),key=lambda x:x[1])[::-1]
        cnt = 0
        tot =0
        for i, j in cntr:
            tot +=j
            cnt +=1
            if tot >=half:
                return cnt


        