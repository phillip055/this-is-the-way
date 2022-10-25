# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class NodeInfo:
    def __init__(self, maxDiameter, maxDepth):
        self.maxDiameter = maxDiameter
        self.maxDepth = maxDepth

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def DBT(root):
            if root:
                p = DBT(root.left)
                q = DBT(root.right)
                
                maxD = p.maxDepth + q.maxDepth
                
                
                return NodeInfo(
                    max(maxD, p.maxDiameter, q.maxDiameter),
                    1 + max(p.maxDepth, q.maxDepth)
                )
            else:
                return NodeInfo(0, 0)
        return DBT(root).maxDiameter
                    
