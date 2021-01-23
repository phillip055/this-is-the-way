# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1: TreeNode, t2: TreeNode):
            if (t1 == None and t2 == None):
                return True
            elif(t1 == None or t2 == None):
                return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t2.right, t1.left)
            
        return isMirror(root, root)
