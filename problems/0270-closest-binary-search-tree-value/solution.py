# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        distances = {}
        def helper(root, target, prev=float('-inf')):
            if not root:
                return
            distance = target - root.val
            distances[root.val] = abs(distance)
            if root.val < target:
                distance = helper(root.right, target, prev=distance)
            else:
                distance = helper(root.left, target, prev=distance)
        helper(root, target)
        min_k = None
        min_v = float('inf')
        for k, v in distances.items():
            if v == min_v:
                if k < min_k:
                    min_k, min_v = k, v
            elif v < min_v:
                min_k, min_v = k, v
        return min_k
                
        
