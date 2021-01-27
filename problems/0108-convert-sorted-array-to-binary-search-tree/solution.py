# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def solve(nums, left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(nums[left])
            mid = (left + right) >> 1
            root = TreeNode(nums[mid])
            root.left = solve(nums, left, mid - 1)
            root.right = solve(nums, mid + 1, right)
            return root
            
        
        left = 0
        right = len(nums) - 1
        return solve(nums, 0, right)
