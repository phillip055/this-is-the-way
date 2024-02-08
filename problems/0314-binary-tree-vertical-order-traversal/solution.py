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
        cols = defaultdict(list)
        
        q = deque([(root, 0)])
        min_col, max_col = 0, 0
        while len(q):
            node, col = q.popleft()
            cols[col].append(node.val)
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
        result = []
        for col in range(min_col, max_col + 1):
            result.append(cols[col])
        return result
            
