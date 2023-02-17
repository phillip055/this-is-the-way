# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            arr.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        
        minDiff = float('inf')
        for i in range(1, len(arr)):
            minDiff = min(minDiff, abs(arr[i] - arr[i-1]))
        return minDiff

