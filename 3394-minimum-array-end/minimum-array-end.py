class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # make b into every bit not set in x

        b=1
        n-=1
        ret=x
        while n:
            if b&x==0:
                if n&1:
                    ret|=b
                n>>=1
            b<<=1


        

        return ret
        