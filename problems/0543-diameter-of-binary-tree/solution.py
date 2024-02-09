# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if root is None:
                return (0, 0)
            
            lpath, ldiameter = helper(root.left)
            rpath, rdiameter = helper(root.right)
            
            path = 1 + max(lpath, rpath)
            diameter = max(ldiameter, rdiameter, lpath + rpath)
            
            return path, diameter
        
        p, d = helper(root)
        
        return d
            
