# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        answer = []
        
        q.append(root)
        
        while(q):
            
            size = len(q)
            current_level = []
            for _ in range(size):
                node = q.popleft()
                current_level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            answer.append(current_level)
            
        return answer[::-1]
        
