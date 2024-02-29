# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s, nodes = 0, [root]
        while nodes:
            node, nodes = nodes[0], nodes[1:]
            if node.val>=low and node.val<=high:
                s += node.val
            if node.right: nodes = [node.right] + nodes
            if node.left: nodes = [node.left] + nodes
        return s 