class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        S = ''
        while i < len(s):
            S += s[i:i + k][::-1]
            S += s[i + k:i + k + k]
            i += k + k
        return S