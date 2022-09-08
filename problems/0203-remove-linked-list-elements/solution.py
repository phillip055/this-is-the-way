# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        newHead = ListNode(-1, next=head)
        curr = newHead
        while curr != None:
            nextElem = curr.next
            while nextElem != None and nextElem.val == val:
                nextElem = nextElem.next
            curr.next = nextElem
            curr = curr.next
        return newHead.next
