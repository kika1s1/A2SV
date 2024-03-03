class Solution:
    def customSortString(self, order: str, s: str) -> str:
        st = set(s)
        odr = set(order)
        ans = ""
        for i in order:
            if i in st:
                ans +=i*s.count(i)
        for i in s:
            if i not in odr:
                ans +=i
        return ans
        