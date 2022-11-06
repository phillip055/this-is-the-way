# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
                
        def length(head):
            if not head: return 0
            return 1 + length(head.next)
        dummy = ListNode(0,head)
        temp1, temp2 = dummy, dummy
        n = length(dummy)
        
        for _ in range(k-1): temp1 = temp1.next
        for _ in range(n-k-1): temp2 = temp2.next
        
        temp1.next, temp2.next = temp2.next, temp1.next
        temp1.next.next, temp2.next.next = temp2.next.next, temp1.next.next
        return dummy.next

        
        
        
