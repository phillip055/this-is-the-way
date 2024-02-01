# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = {None: 0}
        
        def dd(root, parent=None):
            if not root:
                return
            depth[root] = depth[parent] + 1
            dd(root.left, root)
            dd(root.right, root)
        
        dd(root)
        max_depth = max(depth.values())

        def lca(root):
            if root == None:
                return None
            if depth[root] == max_depth:
                return root
            l = lca(root.left)
            r = lca(root.right)
            if l and r:
                return root
            return l or r
        return lca(root)


