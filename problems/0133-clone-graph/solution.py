"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        mapping = {node.val: Node(node.val, [])}
        exploring = [node]
        while len(exploring):
            _node = exploring.pop(0)
            clone_node = mapping[_node.val]
            for n in _node.neighbors:
                if n.val not in mapping:
                    mapping[n.val] = Node(n.val, [])
                    exploring.append(n)
                clone_node.neighbors.append(mapping[n.val])
        return mapping[node.val]

