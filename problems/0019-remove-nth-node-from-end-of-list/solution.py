# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        left = d
        right = head
        
        for i in range(n):
            right = right.next
        
        while right:
            right = right.next
            left = left.next
            
        print(left.val)
            
        left.next = left.next.next
        return d.next
