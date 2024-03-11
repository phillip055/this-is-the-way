# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        to_explore = deque([(root, 0)])
        cols = defaultdict(list)
        min_col = float('inf')
        max_col = float('-inf')
        while len(to_explore):
            node, col = to_explore.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            cols[col].append(node.val)
            if node.left:
                to_explore.append((node.left, col - 1))
            if node.right:
                to_explore.append((node.right, col + 1))
        result = []
        for col_idx in range(min_col, max_col + 1):
            result.append(cols[col_idx])
        
        return result

        

