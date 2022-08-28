# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = curr = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        if list1 != None:
            curr.next = list1
        else:
            curr.next = list2
        return result.next
            
# def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:     
#         result = new = ListNode()
#         while list1 and list2:
#             if list1.val < list2.val:
#                 new.next = list1
#                 list1 = list1.next
#             else:
#                 new.next = list2
#                 list2 = list2.next
#             new = new.next
#         if list1:
#             new.next = list1
#         else:
#             new.next = list2
#         return result.next
