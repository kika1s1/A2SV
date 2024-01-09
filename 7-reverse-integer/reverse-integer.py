class Solution:
    def reverse(self, x: int) -> int: 
        MIN, MAX = -2**31, 2**31-1
        ans = 0
        b = abs(x)
        l = len(str(b))
        times = -1 if x < 0 else 1
        x = abs(x)
        pw = 0
        while x >= 1:
            rem = x % 10
            pw += 1
            ans += rem * (10 ** (l-pw))

            x //= 10
        if ans > MAX:
            return 0
        if x < MIN:
            return 0
        return ans*times
