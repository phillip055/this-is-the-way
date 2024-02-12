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
            if root is None:
                return (0, 0) # sum, count
            
            lsum, lcount = helper(root.left)
            rsum, rcount = helper(root.right)
            
            tsum = root.val + lsum + rsum
            tcount = lcount + rcount + 1

            if tsum // tcount == root.val:
                count += 1

            return tsum, tcount 
        
        helper(root)
        return count
            
            

