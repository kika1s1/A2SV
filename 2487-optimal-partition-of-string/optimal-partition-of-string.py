class Solution:
    def partitionString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = []
        counter = 1
        for i in range(len(s)):
            if len(ans) == 0:
                ans.append(s[i])
            elif s[i] not in ans:
                ans.append(s[i])
            elif s[i] in ans:
                counter += 1
                ans.clear()
                ans.append(s[i])
        return counter
