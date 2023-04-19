# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longestPath = 0
        
        def rec(root, left, count):
            if root:
                self.longestPath = max(self.longestPath, count)
                if left:
                    rec(root.left, False, count + 1)
                    rec(root.right, True, 1)
                else:
                    rec(root.left, False, 1)
                    rec(root.right, True, count + 1)
        
        rec(root, False, 0)
        rec(root, True, 0)
        return self.longestPath


