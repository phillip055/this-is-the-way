# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, tree: Optional[TreeNode],min=float('-inf'), max=float('inf')) -> bool:
        if tree == None:
            return True
        if min >= tree.val or tree.val >= max:
            return False
        return (
            self.isValidBST(tree.left, min, tree.val)
            and 
            self.isValidBST(tree.right, tree.val, max)
        )
