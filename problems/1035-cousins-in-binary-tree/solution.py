# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        h = {}
        def helper(root, depth=0, parent=None):
            if root == None:
                return
            h[root.val] = (depth, parent)
            helper(root.left, depth + 1, root.val)
            helper(root.right, depth + 1, root.val)
        
        helper(root)
        if h[x][0] == h[y][0] and h[x][1] != h[y][1]:
            return True
        return False

