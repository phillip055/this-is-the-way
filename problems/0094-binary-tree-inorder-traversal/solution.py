# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def helper(root):
            nonlocal result
            if not root:
                return 0
            helper(root.left)
            result.append(root.val)
            helper(root.right)
        helper(root)
        return result
