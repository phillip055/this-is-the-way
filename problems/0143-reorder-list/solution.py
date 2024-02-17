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
        def r(h):
            p = None
            c = h
            while c:
                t = c.next
                c.next = p
                p = c
                c = t
            return p


        curr = head
        count = 1
        while curr:
            curr = curr.next
            count += 1
        mid = count //2
        
        curr = head
        prev = None
        while mid > 0:
            mid -= 1
            prev = curr
            curr = curr.next
        
        prev.next = None
        l1 = head
        l2 = r(curr)
        res = ListNode()
        while l1 and l2:
            res.next = l1
            l1 = l1.next
            res = res.next
            
            res.next = l2
            l2 = l2.next
            res = res.next
        while l1:
            res.next = l1
            l1 = l1.next
            res = res.next
        while l2:
            res.next = l2
            l2 = l2.next
            res = res.next



