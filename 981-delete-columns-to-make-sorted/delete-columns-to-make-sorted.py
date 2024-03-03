class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        x=0
        print(zip(strs))
        for i in zip(*strs):
            if list(i)!=sorted(i):
                x+=1
                
        return x
       
       
        