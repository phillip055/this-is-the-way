# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depths = defaultdict(list)
        def depth(root, height=0):
            if not root:
                return
            depths[height].append(root)
            depth(root.left, height + 1)
            depth(root.right, height + 1)
        
        depth(root)
        
        max_depth = max(depths)
        deepest_nodes = depths[max_depth]
        
        def lca(root):
            if not root or root in deepest_nodes:
                return root
            left = lca(root.left)
            right = lca(root.right)
            if left and right:
                return root
            return left or right
        
        return lca(root)

