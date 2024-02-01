# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root:
            return root
        
        left = None
        right = None
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:    
            return self.lowestCommonAncestor(root.right, p, q)

        left = self.lowestCommonAncestor(root.left, p, q)
        right =  self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

