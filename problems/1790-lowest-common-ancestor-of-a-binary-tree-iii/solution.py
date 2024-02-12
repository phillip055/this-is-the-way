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
            h = 0
            while node:
                h += 1
                node = node.parent
            return h
        
        ph = height(p)
        qh = height(q)

        while ph < qh:
            q = q.parent
            qh -= 1
        
        while qh < ph:
            p = p.parent
            ph -= 1
        
        while p != q:
            p = p.parent
            q = q.parent
        return p
        
