# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(_root, s = ""):
            s += str(_root.val)
            if not _root.left and not _root.right:
                result.append(s)
                return
            if _root.left:
                dfs(_root.left, s + "->")
            if _root.right:
                dfs(_root.right, s + "->")
            
        dfs(root)
        return result
