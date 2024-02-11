# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if root is None:
                return (0, float("-inf"))
            leftMaxPath, leftMaxTree = helper(root.left)
            rightMaxPath, rightMaxTree = helper(root.right)
            max_path_till_now = max(leftMaxPath, rightMaxPath)
            max_path = max(max_path_till_now + root.val, root.val)
            max_tree = max(leftMaxTree, rightMaxTree, leftMaxPath + rightMaxPath + root.val, root.val, max_path)
            return max_path, max_tree
        
        res = helper(root)
        return res[1]

