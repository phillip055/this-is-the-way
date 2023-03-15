# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        toExplore = [root]
        while len(toExplore):
            node = toExplore.pop(0)
            if node is None:
                for e in toExplore:
                    if e != None:
                        return False
                return True
            toExplore.append(node.left)
            toExplore.append(node.right)
        return True



