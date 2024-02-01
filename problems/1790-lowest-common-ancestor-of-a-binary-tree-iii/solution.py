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

        def height(node):
            if not node:
                return 0
            return 1 + height(node.parent)
        
        ph = height(p)
        qh = height(q)    

        while ph > qh:
            ph -= 1
            p = p.parent
        
        while qh > ph:
            qh -= 1
            q = q.parent
        
        while p != q:
            p = p.parent
            q = q.parent
        return p

    
