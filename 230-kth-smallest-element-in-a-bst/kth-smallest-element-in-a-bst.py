# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        heap  = []
        def dfs(root):
            nonlocal cnt
            if not root:
                return 
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            if cnt == k:
                heappush(heap, -root.val)     
                heappop(heap)
            else:
                heappush(heap, -root.val)
                cnt +=1
            
        dfs(root)
        return -heappop(heap)

                
