class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        flist=[1]
        value=0
        while True and flist[-1]<k:
            flist.append(value+flist[-1])
            value=flist[-2]
        j=len(flist)-1
        count=0
        while j>=0 and k>0:
            if flist[j]<=k:
                k-=flist[j]
                count+=1
            j-=1
        return (count)
        