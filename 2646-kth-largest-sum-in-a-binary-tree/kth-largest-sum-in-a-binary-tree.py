
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        levelSum = []
        queue = deque([root])
        while queue:
            cnt = 0
            level_size = len(queue) 
            for _ in range(level_size):
                node = queue.popleft()
                cnt += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levelSum.append(cnt)
        
        levelSum.sort(reverse=True)
        if k <= len(levelSum):
            return levelSum[k-1]
        return -1
