"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def depth(root):
            if not root or not root.parent:
                return 0
            return 1 + depth(root.parent)
        
        pd = depth(p)
        qd = depth(q)
        
        while pd > qd:
            pd -= 1
            p = p.parent
        
        while qd > pd:
            qd -= 1
            q = q.parent
        
        while p != q:
            p = p.parent
            q = q.parent
        
        return p

