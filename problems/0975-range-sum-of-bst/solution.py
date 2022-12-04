# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(node, low, high):
            result = 0
            if node == None:
                return result
            if node.val >= low and node.val <= high:
                result += node.val
            if node.left:
                result += helper(node.left, low, high)
            if node.right:
                result += helper(node.right, low, high)
            return result

        return helper(root, low, high)
