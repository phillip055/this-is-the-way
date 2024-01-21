# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        c = root.val

        while root:
            if abs(root.val - target) < abs(c - target):
                c = root.val
            elif abs(root.val - target) == abs(c - target) and root.val < c:
                c = root.val
            else:
                if target > root.val:
                    root = root.right
                else:
                    root = root.left
        return c
