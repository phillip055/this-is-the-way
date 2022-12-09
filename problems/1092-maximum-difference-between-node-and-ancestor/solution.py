# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if root == None:
                return float('-inf')
            curr = max(abs(lower-root.val), abs(upper-root.val))
            newLower = min(lower, root.val)
            newUpper = max(upper, root.val)
            childMax = max(
                helper(root.left,lower=newLower, upper=newUpper),
                helper(root.right,lower=newLower, upper=newUpper),
            )
            return max(childMax, curr)
        
        return helper(root, lower=root.val, upper=root.val)
