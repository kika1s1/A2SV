class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range((n//2)+1):
            if 3**i ==n:
                return True
            if 3**i > n:
                return False