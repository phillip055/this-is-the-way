# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, _max=float('-inf')) -> int:
        if root == None:
            return 0
        count = 0
        if root.val >= _max:
            count += 1
            _max = root.val
        count += self.goodNodes(root.left, _max)
        count += self.goodNodes(root.right, _max)
        return count
