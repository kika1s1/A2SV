class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = ''
        curr = ''
        for i in range(len(s)):
            if s[i].isalpha() == True:
                curr += s[i]
        ind = -1
        for i in range(len(s)):
            if s[i].isalpha() == True:
                ans += curr[ind]
                ind -= 1
            else:
                ans += s[i]
        return ans