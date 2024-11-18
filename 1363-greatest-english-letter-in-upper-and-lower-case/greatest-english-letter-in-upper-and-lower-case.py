class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = []
        chars = set(s)
        for char in chars:
            if char.isupper() and char.lower() in chars:
                ans.append(char)
        ans.sort()
        if not ans:
            return ""
        return ans[-1]