# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
              
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
          
            nonlocal moves_count
            moves_count += abs(left_balance) + abs(right_balance)

            return left_balance + right_balance + node.val - 1

        moves_count = 0
        dfs(root)
        return moves_count

