# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        nums=[]
        def preOrder(root, nums):
            if not root:
                return
            nums.append(root.val)
            if root.left is not None:
                preOrder(root.left, nums)
            if root.right is not None:
                preOrder(root.right, nums)
        preOrder(root, nums)
        nums.sort()
        def helper(left,right):
            if left>right:
                return None
            mid=(left+right)//2    
            root=TreeNode(nums[mid])
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root    
        return helper(0,len(nums)-1) 
        