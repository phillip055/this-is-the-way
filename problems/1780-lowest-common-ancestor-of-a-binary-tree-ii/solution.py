# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root):
            if not root or root == p or root == q:
                return root
            left = lca(root.left)
            right = lca(root.right)
            if right and left:
                return root
            return left or right
        
        ancestor = lca(root)
        
        def dfs(root, target):
            if root == None:
                return False
            if root == target:
                return True
            return dfs(root.left, target) or dfs(root.right, target)

        if ancestor == q:
            if dfs(ancestor, p):
                return q
            return None
        
        if ancestor == p:
            if dfs(ancestor, q):
                return p
            return None
        
        return ancestor


