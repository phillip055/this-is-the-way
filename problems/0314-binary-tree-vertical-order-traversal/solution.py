# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        to_explore = [(root, 0)]
        groups = defaultdict(list)
        while len(to_explore):
            node, col = to_explore.pop(0)
            if not node:
                continue
            groups[col].append(node.val)
            to_explore.append((node.left, col - 1))
            to_explore.append((node.right, col + 1))
        thi = dict(sorted(groups.items())).values()
        return thi
 
