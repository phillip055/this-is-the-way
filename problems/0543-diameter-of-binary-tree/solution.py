# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root:
                return 0, 0
            l_max_path, l_max_diameter = helper(root.left)
            r_max_path, r_max_diameter = helper(root.right)
            diameter = l_max_path + r_max_path
            path = 1 + max(l_max_path, r_max_path)
            return path, max(l_max_diameter, r_max_diameter, diameter)
        res = helper(root)
        return res[1]
