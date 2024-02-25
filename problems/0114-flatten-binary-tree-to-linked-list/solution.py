# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None
        return right or left or root

