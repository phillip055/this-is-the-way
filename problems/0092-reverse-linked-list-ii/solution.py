# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        dummy = ListNode(0, None)
        dummy.next = head
        leftPtr = dummy
        
        for _ in range(left-1):
            leftPtr = leftPtr.next
        
        prev, curr = None, leftPtr.next
        for _ in range(right-left + 1):
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        
        leftPtr.next.next = curr
        leftPtr.next = prev
        return dummy.next
        
