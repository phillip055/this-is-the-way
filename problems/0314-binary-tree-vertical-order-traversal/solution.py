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
        to_explore = deque([(root, 0)])
        ch = defaultdict(list)
        
        while len(to_explore):
            node, col = to_explore.popleft()
            ch[col].append(node.val)
            if node.left:
                to_explore.append((node.left, col-1))
            if node.right:
                to_explore.append((node.right, col+1))
        ch = dict(sorted(ch.items()))
        return ch.values()

