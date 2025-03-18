# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums):
            if not nums:
                return
            N = len(nums) 
            root = TreeNode(nums[N//2])
            root.left = build(nums[:N//2])
            root.right = build(nums[(N//2)+1:])
            return root
        return build(nums)