class Solution:
    def minOperations(self, s: str) -> int:
        ans1=ans2=0
        for idx,x in enumerate(s):
            if idx%2==int(x):
                ans1+=1
            else:
                ans2+=1
        return min(ans1,ans2)            