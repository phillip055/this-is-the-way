"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        memo = []
        def rec(node):
            memo.append(node.val)
            for c in node.children:
                rec(c)
        if root:
            rec(root)
        return memo
