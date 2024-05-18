# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        moves = 0

        def helper(root):
            if root is None:
                return 0
            leftRemaining = helper(root.left)
            rightRemaining = helper(root.right)
            
            nonlocal moves
            moves += abs(leftRemaining) + abs(rightRemaining)
            return leftRemaining + rightRemaining + root.val - 1
        
        helper(root)
        return moves

