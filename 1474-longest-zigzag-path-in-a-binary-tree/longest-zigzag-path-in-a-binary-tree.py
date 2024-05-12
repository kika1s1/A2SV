# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxim = 0
        memo = {}
        def countZig(root, is_right, cnt):
            nonlocal memo
            if (root, is_right) in memo:
                return memo[(root, is_right)]
            if not root:
                return 0
            if is_right and root.right:
                cnt = countZig(root.right, not is_right, cnt + 1)

            if not is_right and root.left:
                cnt = countZig(root.left, not is_right, cnt + 1)
            memo[(root, is_right)] = cnt
            return memo[(root, is_right)]

        def dfs(root):
            nonlocal maxim
            if not root:
                return
            cnt_left = countZig(root, True, 0)
            cnt_right = countZig(root, False, 0)
            maxim = max(maxim, cnt_left, cnt_right)
            if root.right:
                dfs(root.right)
            if root.left:
                dfs(root.left)

        dfs(root)
        return maxim