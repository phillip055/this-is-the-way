# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode], count = 0) -> int:
        if not root:
            return count
        if not root.left:
            return 1 + self.minDepth(root.right, count)
        if not root.right:
            return 1 + self.minDepth(root.left, count)
        return 1 + min(
            self.minDepth(root.left, count),
            self.minDepth(root.right, count),
        )

