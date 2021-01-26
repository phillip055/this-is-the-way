"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if (root == None):
            return []
        result = []
        for child in root.children:
            if (child.val != None):
                res = self.postorder(child)
                result.extend(res)
        result.append(root.val)
        return result
