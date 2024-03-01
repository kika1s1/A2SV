class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        path = path.split("/")
        for p in path:
            if p == "":
                continue
            elif p ==".." and len(stack)!=0:
                stack.pop()
            elif p ==".":
                continue
            elif p == ".." and len(stack) == 0:
                continue
            else:
                stack.append(p)
        ans = ""
        for p in stack:
            ans +="/"
            ans +=p
        return ans if ans !="" else "/"