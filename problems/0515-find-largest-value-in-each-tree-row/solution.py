# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        result = []
        while len(queue):
            current_max = float('-inf')
            for idx in range(len(queue)):
                node = queue.pop(0)
                if node.val > current_max:
                    current_max = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_max)
        return result
                
                
        
