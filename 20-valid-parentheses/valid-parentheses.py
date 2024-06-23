class Solution:
    def isValid(self, s: str) -> bool:
        close = {"(":")", "[":"]", "{":"}"}
        stack = []
        for i in s:
            if i in close:
                stack.append(i)
            else:
                if stack and close[stack[-1]] == i:
                    stack.pop()
                else:
                    return False


        return len(stack) ==0