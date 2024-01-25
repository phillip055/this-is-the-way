# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return 0
            hl = helper(root.left)
            if hl == -1:
                return -1
            hr = helper(root.right)
            if hr == -1:
                return -1
            if abs(hl - hr) > 1:
                return -1
            return 1 + max(hr, hl)
        if root == None:
            return True
        if helper(root) == -1:
            return False
        return True

