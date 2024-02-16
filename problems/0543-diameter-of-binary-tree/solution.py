# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return 0, 0
            leftLongestPath, leftLongestDiameter = helper(root.left)
            rightLongestPath, rightLongestDiameter = helper(root.right)
            d = leftLongestPath + rightLongestPath
            return 1 + max(leftLongestPath, rightLongestPath), max(d, leftLongestDiameter, rightLongestDiameter)
        _, d = helper(root)
        return d


