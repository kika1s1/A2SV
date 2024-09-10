class Solution:
    def isValid(self, s: str) -> bool:
        map_with_close = { ")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char not in map_with_close:
                stack.append(char)
            else:
                if stack and stack[-1] == map_with_close[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        