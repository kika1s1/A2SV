class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        close_count = 0
        for i in s:
            if i == "(":
                open_count += 1
            elif i == ")" and open_count > 0:
                open_count -= 1
            else:
                close_count += 1
        return open_count + close_count