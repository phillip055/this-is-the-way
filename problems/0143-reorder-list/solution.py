# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        mid = self.reverseList(slow.next)
        slow.next = None

        
        curr1, curr2 = head, mid
        while curr1 or curr2:
            _next1 = curr1.next
            curr1.next = curr2
            curr1 = curr2
            curr2 = _next1
        return head
        
            
        
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr != None:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return prev
        
