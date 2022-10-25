# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        def helper(root, wall):
            if root == None:
                return 0
            if root.val >= wall:
                return 1 + helper(root.left, root.val) + helper(root.right, root.val)
            else:
                return helper(root.left, wall) + helper(root.right, wall)
        return helper(root, root.val)
