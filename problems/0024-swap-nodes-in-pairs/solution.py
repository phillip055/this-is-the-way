# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        curr = head
        _next = curr.next
        _next_next = _next.next
        
        _next.next = curr
        curr.next = self.swapPairs(_next_next)
        
        return _next
