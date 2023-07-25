# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        queue = [(root, "right")]
        _sum = 0

        while queue:
            node, side = queue.pop(0)
            if node.left:
                queue.append((node.left, "left"))
            if node.right:
                queue.append((node.right, "right"))
            if not node.left and not node.right and side == "left":
                _sum += node.val
        return _sum

