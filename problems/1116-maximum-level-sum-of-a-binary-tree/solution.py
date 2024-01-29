# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        to_explore = deque([root])
        level = 0
        max_level = 0
        max_sum = float('-inf')

        while len(to_explore):
            level += 1
            s = 0
            for idx in range(len(to_explore)):
                node = to_explore.popleft()
                s += node.val
                if node.left:
                    to_explore.append(node.left)
                if node.right:
                    to_explore.append(node.right)
            if s > max_sum:
                max_sum = s
                max_level = level
        return max_level

