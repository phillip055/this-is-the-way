# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        to_explore = deque([(root, 1)])
        
        while len(to_explore):
            node, level = to_explore.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                to_explore.append((node.left, level + 1))
            if node.right:
                to_explore.append((node.right, level + 1))
        return 1
        
