# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def pre(root):
            if not root:
                return 

            ans.append(root.val)
            if root.left:
                pre(root.left)
            if root.right:
                pre(root.right)
            return ans
        return pre(root)
        