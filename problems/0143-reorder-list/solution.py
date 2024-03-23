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
        count = 0
        curr = head
        while curr is not None:
            curr = curr.next
            count += 1
        
        mid = (count // 2) - 1
        curr = head
        while mid > 0:
            curr = curr.next
            mid -= 1
        
        first = head
        second = curr.next
        curr.next = None
        
        def reverse(node):
            curr = node
            prev = None
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        second = reverse(second)
        new_head = ListNode()
        while first or second:
            if first:
                new_head.next = first
                new_head = new_head.next
                first = first.next
            if second:
                new_head.next = second
                new_head = new_head.next
                second = second.next
        return new_head.next


