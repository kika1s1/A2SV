# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMinOfRight(root):
            current = root
            while current.left:
                current = current.left
            return current

        def delNode(root, key):
            if not root:
                return root
            if key < root.val:
                root.left = delNode(root.left, key)
            elif key > root.val:
                root.right = delNode(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                temp = findMinOfRight(root.right)
                root.val = temp.val
                root.right = delNode(root.right, temp.val) 
            return root
        return delNode(root, key)
