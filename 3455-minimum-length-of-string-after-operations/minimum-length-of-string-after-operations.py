class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for rep in cnt.values():
            if rep %2 == 1:
                ans +=1
            else:
                ans +=2
        return ans
                