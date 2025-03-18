# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        index_value = defaultdict(lambda:float("-inf"))
        def dfs(current_root, level):
            if current_root:
                index_value[level] = max(index_value[level], current_root.val)
                if current_root.left:
                    dfs(current_root.left, level+1)
                if current_root.right:
                    dfs(current_root.right, level+1)
        dfs(root, 1)
        return list(index_value.values())