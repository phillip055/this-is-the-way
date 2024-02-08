"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

# case 1
# prev <= val <= curr
# case 2
# prev > curr
# # val >= prev or val <= curr

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        
        prev, curr = head, head.next
        while True:
            insertTo = False
            if prev.val <= insertVal <= curr.val:
                insertTo = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    insertTo = True
            
            if insertTo:
                prev.next = Node(insertVal, curr)
                return head
            
            prev, curr = curr, curr.next
            if prev == head:
                break
        prev.next = Node(insertVal, curr)

        return head


