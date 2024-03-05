class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                checker  = set(s[i:j+1])
                if all(i in checker for i in sub.swapcase()):
                    if len(ans) < len(sub):
                        ans = sub
        return ans