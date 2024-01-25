# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def helper(root):
            nonlocal count
            if not root:
                return (0, 0)
            ts = 0
            tc = 0
            avg = helper(root.left)
            ts += avg[0]
            tc += avg[1]
            avg = helper(root.right)
            ts += avg[0]
            tc += avg[1]
            ts += root.val
            tc += 1
            if (ts//tc) == root.val:
                count += 1
            return ts, tc
        helper(root)
        return count
        

    
