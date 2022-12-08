# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaves):
            if root == None:
                return 
            if root.left == None and root.right == None:
                leaves.append(root.val)
                return
            dfs(root.left, leaves)
            dfs(root.right, leaves)
        leftLeaves = []
        dfs(root1, leftLeaves)
        rightLeaves = []
        dfs(root2, rightLeaves)

        print(leftLeaves)
        print(rightLeaves)
        return leftLeaves == rightLeaves


