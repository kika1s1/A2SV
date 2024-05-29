class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s,2)

        # print(n)
        cnt = 0
        while n !=1:
            cnt  +=1
            if n % 2 ==1:
                n = n+ 1
            else:
                n //=2
        return(cnt)

        