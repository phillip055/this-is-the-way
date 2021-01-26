# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if (t1 == None and t2 == None):
            return None
        
        if (t1 == None):
            t1_value = 0
        else:
            t1_value = t1.val
        if (t2 == None):
            t2_value = 0
        else:
            t2_value = t2.val
            
        t1_left = t1.left if t1 != None else None
        t2_left = t2.left if t2 != None else None
        t1_right = t1.right if t1 != None else None
        t2_right = t2.right if t2 != None else None
        
        return TreeNode(t1_value + t2_value, self.mergeTrees(t1_left, t2_left), self.mergeTrees(t1_right, t2_right))
