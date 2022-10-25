# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(root, subRoot):
            if (not root) or (not subRoot):
                return root is None and subRoot is None
            return root.val == subRoot.val and isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)
        
        toExplore = [root]
        while len(toExplore):
            node = toExplore.pop(0)
            if node.left:
                toExplore.append(node.left)
            if node.right:
                toExplore.append(node.right)
            if isIdentical(node, subRoot):
                return True
        return False
