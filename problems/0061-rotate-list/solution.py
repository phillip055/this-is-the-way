# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if k == 0:
            return head
        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next
        curr.next = head
        
        k= length - (k%length)
        for _ in range(k):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        return newHead
        
