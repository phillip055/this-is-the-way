"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        first, last = None, None
        
        def helper(root):
            nonlocal first, last
            if root is None:
                return
            helper(root.left)
            if last:
                last.right = root
                root.left = last
            else:
                first = root
            last = root
            helper(root.right)
    
        helper(root)
        first.left = last
        last.right = first
        return first


