# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode(-1)
        even_head = ListNode(-1)
        def traversal(curr, even_tail, odd_tail):
            if not curr:
                return
            if curr:
                odd_tail.next = curr
                curr = curr.next
                odd_tail = odd_tail.next
                odd_tail.next = None
            if curr:
                even_tail.next = curr
                curr = curr.next
                even_tail = even_tail.next
                even_tail.next = None
            traversal(curr, even_tail, odd_tail)
        
        traversal(head, odd_head, even_head)
        
        print(odd_head)
        print(even_head)
        curr = even_head
        while curr.next:
            curr = curr.next
        even_tail = curr
        even_tail.next = odd_head.next
        return even_head.next
            
        
