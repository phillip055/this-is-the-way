# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def pre(root, arr=[]):
            if root:
                pre(root.left)
                arr.append(root.val)
                pre(root.right)
            return arr
        arr = pre(root)
        a = sorted(arr)
        return a[k-1]
        
        
