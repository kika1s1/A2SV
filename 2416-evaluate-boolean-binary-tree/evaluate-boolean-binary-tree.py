# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def dfs(root):
            if not root:
                return 
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            ans.append(root.val)
        dfs(root)
        stack = []
        for i in ans:
            if i == 1 or  i == 0:
                stack.append(i)
            else:
                first = stack.pop()
                second = stack.pop()
                if i == 2:
                    stack.append(first | second) 
                else:
                     stack.append(first & second)
        

        return stack[-1]
        