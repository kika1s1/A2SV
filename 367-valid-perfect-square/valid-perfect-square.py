class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num) == int(sqrt(num))