class Solution:
    def makeFancyString(self, s: str) -> str:
        top = 0
        stack = []
        cnt = 0
        for char in s:
            if not stack:
                top = 1
                stack.append(char)
            elif stack and stack[-1] == char and top >=2:
                cnt +=1
            elif stack and stack[-1] !=char:
                top = 1
                stack.append(char)
            elif stack and stack[-1] ==char and top < 2:
                top +=1
                stack.append(char)
        return "".join(stack)