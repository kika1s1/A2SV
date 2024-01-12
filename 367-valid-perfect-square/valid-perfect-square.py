class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return sqrt(num) == int(sqrt(num))
        # for i in range(num+1):
        #     if i*i == num:
        #         return True
        # return False
        s=int(num**0.5)
        return s*s==num
