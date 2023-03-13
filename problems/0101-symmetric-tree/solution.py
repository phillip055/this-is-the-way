# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSame(one, two):
            if one and two:
                return one.val == two.val and isSame(one.left, two.right) and isSame(one.right, two.left)
            if not one and not two:
                return True
            return False
        
        return isSame(root.left, root.right)
            



            
        
        

        
