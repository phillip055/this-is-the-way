"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}

        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new = oldToNew[curr]
            _next = oldToNew[curr.next]
            _random = oldToNew[curr.random]
            new.next = _next
            new.random = _random
            curr = curr.next
        return oldToNew[head]

