# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)])
        cols = defaultdict(list)
        
        while len(q):
            node, col = q.popleft()
            cols[col].append(node.val)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
        
        sorted_keys = sorted(dict(cols.items()))
        result = []
        for key in sorted_keys:
            result.append(cols[key])
        return result
        

