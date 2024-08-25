# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def postOrder(root):
            if not root:
                return 
            if root.left:
                postOrder(root.left)
            if root.right:
                postOrder(root.right)
            ans.append(root.val)
        postOrder(root)
        return ans

        
        