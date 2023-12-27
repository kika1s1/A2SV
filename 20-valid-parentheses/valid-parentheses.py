class Solution(object):
    def isValid(self, s):
        pair = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for i in s:
            check = pair.get(i, 0)
            if check == 0 and len(stack) == 0:
                return False
            if i in pair:
                stack.append(i)
            elif stack:
                if i == pair[stack[-1]]:
                    stack.pop()
                else:
                    return False
        print(stack)
        return len(stack) == 0