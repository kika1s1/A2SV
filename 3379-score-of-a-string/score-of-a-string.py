class Solution:
    def scoreOfString(self, s: str) -> int:
        diff = []
        for i in range(len(s)-1):
            b = ord(s[i])-ord(s[i+1])
            diff.append(abs(b))
        return sum(diff)