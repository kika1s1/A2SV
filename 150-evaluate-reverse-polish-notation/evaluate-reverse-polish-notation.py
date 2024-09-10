class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "-", "/", "*"}
        stack = []
        
        for d in tokens:
            if d in op:
                first = stack.pop()
                second = stack.pop()
                if d == "/":
                    ans = str(int(int(second) / int(first)))
                else:
                    ans = str(eval(second + d + first))
                stack.append(ans)
            else:
                stack.append(d)
        
        return int(stack[-1])
