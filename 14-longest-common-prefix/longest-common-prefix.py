class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        ans = ""
        r = 1
        for i in strs[0]:
            sub = strs[0][:r]
            if all(st[:r] == sub for st in strs):
                ans = sub
                r += 1
        return ans
