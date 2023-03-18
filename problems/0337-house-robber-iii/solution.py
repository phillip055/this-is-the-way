# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def rec(root, taken_prev=False):
            if not root:
                return 0
            if taken_prev:
                return rec(root.left, False) + rec(root.right, False)
            else:
                return max(
                    root.val + rec(root.left, True) + rec(root.right, True),
                    rec(root.right, False) + rec(root.left, False),
                )
        return rec(root)

