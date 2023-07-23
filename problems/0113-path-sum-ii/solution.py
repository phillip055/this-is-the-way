# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(root, targetSum, currentPath):
            if not root:
                return None
            targetSum -= root.val
            currentPath.append(root.val)
            if not root.left and not root.right and targetSum == 0:
                result.append(currentPath)
            dfs(root.left, targetSum, currentPath[:])
            dfs(root.right, targetSum, currentPath[:])
        dfs(root, targetSum, [])
        return result

