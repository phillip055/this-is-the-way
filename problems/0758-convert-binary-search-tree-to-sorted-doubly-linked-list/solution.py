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
        def helper(root):
            nonlocal first, last
            if root is None:
                return
            helper(root.left)

            if last:
                root.left = last
                last.right = root
            else:
                first = root
            
            last = root

            helper(root.right)
        first, last = None, None
        if root is None:
            return None
        helper(root)
        first.left = last
        last.right = first
        return first

