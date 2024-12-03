class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        spaces = set(spaces)
        for index, char in enumerate(s):
            if index in spaces:
                ans.append(" ")
                ans.append(char)
            else:
                ans.append(char)
        return "".join(ans)