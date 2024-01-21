"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head == None:
            node = Node(insertVal)
            node.next = node
            return node
        if head.next == None:
            return Node(insertVal, head)

        curr = head.next
        prev = head
        while prev.next != head:
            if prev.val <= insertVal <= curr.val:
                break

            if prev.val > curr.val and (insertVal > prev.val or insertVal < curr.val):
                break
            
            prev, curr = prev.next, curr.next

        # Insert node.
        prev.next = Node(insertVal, curr)
        return head


