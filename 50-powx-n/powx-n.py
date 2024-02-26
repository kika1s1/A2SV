class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(y,pow):
            if pow == 1:
                return y
            if pow == 0:
                return 1
            if pow <0:
                return 1/helper(y,-pow)
            if pow % 2 ==0:
                half = helper(y, pow//2)
                return half*half
            else:
                half = helper(y, (pow-1)//2)
                return half*half * y


        return helper(x, n)