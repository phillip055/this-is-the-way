# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left = root)
        to_explore = [(root, 1)]
        while len(to_explore):
            new_level = []
            for idx in range(len(to_explore)):
                node, d = to_explore[idx]
                if d == depth - 1:
                    l = TreeNode(val)
                    l.left = node.left
                    node.left = l
                    r = TreeNode(val)
                    r.right = node.right
                    node.right = r
                else:
                    if node.left:
                        new_level.append((node.left, d + 1))
                    if node.right:
                        new_level.append((node.right, d + 1))
            to_explore = new_level
        return root


