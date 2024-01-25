# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = [root]
        result = []

        while len(q):
            next_level = []
            total = 0
            for idx in range(len(q)):
                total += q[idx].val
                if q[idx].left:
                    next_level.append(q[idx].left)
                if q[idx].right:
                    next_level.append(q[idx].right)
            result.append(total / len(q))
            q = next_level
        return result


