class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        for p in paths:
            if ".." == p:
                if stack:
                    stack.pop()
            elif "..."  in p:
                stack.append(p)
            elif "/" in p or p == "." or p =="":
                continue
            else:
                stack.append(p)
        print(stack)
        return "/"+"/".join(stack)


