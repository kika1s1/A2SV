class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = 0
        for i in s:
            if i == c:
                cnt +=1
        return (cnt*(cnt+1))//2
                