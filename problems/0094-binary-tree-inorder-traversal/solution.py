# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root == None:
#             return _list
        
#         self.inorderTraversal(root.left, _list)
        
#         _list.append(root.val)
        
#         self.inorderTraversal(root.right, _list)
        
#         return _list
        stack = []
        _list = []
        while root != None or len(stack):
            while (root != None):
                stack.append(root)
                root = root.left
            root = stack.pop()
            _list.append(root.val)
            root = root.right
        return _list
            
            
        
            
            
