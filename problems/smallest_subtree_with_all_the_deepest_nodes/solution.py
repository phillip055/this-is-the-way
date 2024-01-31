# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        heights = defaultdict(list)
        def lca(root, p, q):
            if root in (None, p, q):
                return root
            l = lca(root.left, p, q)
            r = lca(root.right, p, q)
            if l and r:
                return root
            else:
                return l or r
        def dfs(root, h=0):
            if not root:
                return 0
            heights[h].append(root)
            dfs(root.left, 1 + h)
            dfs(root.right, 1 + h)
        dfs(root)
        deepest_depth = max(heights)
        p, q = heights[deepest_depth][0], heights[deepest_depth][-1]
        
        return lca(root, p, q)
            