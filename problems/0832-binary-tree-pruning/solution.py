# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        
        root.left = left
        root.right = right
        
        if left or right or root.val == 1:
            return root
        
        if root.val == 0:
            return None
        
        
            
        
