# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
            
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root == None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            if lh == -1:
                return -1
            if rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)
            
        if root == None:
            return True
        
        if height(root) == -1:
            return False
        return True
            

