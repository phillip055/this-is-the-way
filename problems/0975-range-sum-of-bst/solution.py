# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        s = 0
        if root.val >= low and root.val <= high:
            print(root.val)
            s += root.val
        s += self.rangeSumBST(root.left, low, high)
        s += self.rangeSumBST(root.right, low, high)
        return s
        
        
