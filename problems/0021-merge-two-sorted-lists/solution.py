# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(val=None)
        cursor = head
        cursor1 = list1
        cursor2 = list2
        while cursor1 and cursor2:
            if cursor1.val < cursor2.val:
                cursor.next = cursor1
                cursor1 = cursor1.next
            else:
                cursor.next = cursor2
                cursor2 = cursor2.next
            cursor = cursor.next
        if cursor1:
            cursor.next = cursor1
        if cursor2:
            cursor.next = cursor2
        return head.next
        
