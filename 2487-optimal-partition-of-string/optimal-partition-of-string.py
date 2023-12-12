class Solution:
    def partitionString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = []
        counter = 1
        for i in range(len(s)):
            if s[i] not in ans:
                ans.append(s[i])
            else:
                
                counter += 1
                ans.clear()
                ans.append(s[i])
        return counter
