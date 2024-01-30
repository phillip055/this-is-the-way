# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        to_explore = deque([root])
        result = []
        while len(to_explore):
            level = []
            for _ in range(len(to_explore)):
                node = to_explore.popleft()
                level.append(node.val)
                if node.left:
                    to_explore.append(node.left)
                if node.right:
                    to_explore.append(node.right)
            result.append(level)
        return result

