# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        curr = [root]
        while len(curr):
            result = []
            for i in range(len(curr)):
                node = curr.pop(0)
                if node:
                    result.append(node.val)
                    if node.left:
                        curr.append(node.left)
                    if node.right:
                        curr.append(node.right)
            res.append(result)
        return res
            
