# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxim = 0
        def depth(root, cnt):
            nonlocal maxim
            if not root:
                return 
            maxim = max(cnt, maxim)
            if root.left:
                depth(root.left, cnt+1)
            if root.right:
                depth(root.right, cnt +1)
            return maxim
        return depth(root, 1)