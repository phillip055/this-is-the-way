# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        depths = defaultdict(list)
        
        def dfs(root, depth = 0):
            if not root:
                return
            depths[depth].append(root)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root)
        
        max_height = max(depths)
        
        def lca(root):
            if not root or root in depths[max_height]:
                return root
            left = lca(root.left)
            right = lca(root.right)
            if left and right:
                return root
            return left or right
        
        return lca(root)

