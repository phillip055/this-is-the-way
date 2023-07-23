# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @cache
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, currentSum = 0) -> bool:
        if not root:
            return False
        currentSum += root.val
        if not root.left and not root.right and targetSum == currentSum:
            return True
        return self.hasPathSum(root.left, targetSum, currentSum) or self.hasPathSum(root.right, targetSum, currentSum)

