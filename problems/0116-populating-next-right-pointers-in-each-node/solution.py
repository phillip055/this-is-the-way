"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        toExplore = [root]
        
        while toExplore:
            loops = len(toExplore)
            lvl = []
            for _ in range(loops):
                node = toExplore.pop(0)
                if node.left:
                    toExplore.append(node.left)
                if node.right:
                    toExplore.append(node.right)
                lvl.append(node)
                
            if len(lvl) > 0:
                curr = lvl[0]
                for i in range(1, len(lvl)):
                    curr.next = lvl[i]
                    curr = curr.next
                curr.next = None
        return root
