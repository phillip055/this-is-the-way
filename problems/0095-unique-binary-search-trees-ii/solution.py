# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        @cache
        def helper(start, end):
            if start > end:
                return [None]
            res = []
            for idx in range(start, end + 1):
                leftSubTrees = helper(start, idx - 1)
                rightSubTrees = helper(idx + 1, end)
            
                for left in leftSubTrees:
                    for right in rightSubTrees:
                        root = TreeNode(idx, left, right)
                        res.append(root)
            
            return res
        
        return helper(1, n)
        
