# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)
            left_depth, llca_node = dfs(node.left)
            right_depth, rlca_node = dfs(node.right)
            if left_depth > right_depth:
                return( left_depth + 1,  llca_node)
            elif right_depth > left_depth:
                return (right_depth +1, rlca_node)
            else:
                return (right_depth + 1, node)
        return dfs(root)[1]

        