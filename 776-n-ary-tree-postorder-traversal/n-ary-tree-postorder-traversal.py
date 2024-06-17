"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return 
            for node in root.children:
                dfs(node)
                ans.append(node.val)
            # ans.append(root.val)
            return ans + [root.val]
        return dfs(root)