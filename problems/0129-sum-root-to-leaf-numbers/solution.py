# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        toExplore = [(root, "")]
        res = 0
        while len(toExplore):
            node = toExplore.pop(0)
            node, path = node[0], node[1]
            if node.left is None and node.right is None:
                res += int(path + str(node.val))
                continue
            if node.left:
                toExplore.append((node.left, path + str(node.val)))
            if node.right:
                toExplore.append((node.right, path + str(node.val)))
        return res


