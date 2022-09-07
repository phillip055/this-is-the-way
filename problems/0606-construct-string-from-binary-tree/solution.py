# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""
        _str = str(root.val)
        if root.right:
            if root.left:
                _str += "(" + self.tree2str(root.left) + ")"
            else:
                _str += "()"
            _str += "(" + self.tree2str(root.right) + ")"
        else:
            if root.left:
                _str += "(" + self.tree2str(root.left) + ")"
        return _str
    
            
        
        
