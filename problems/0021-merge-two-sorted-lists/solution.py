# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        
        if (l1.val > l2.val):
            return ListNode(l2.val, self.mergeTwoLists(l2.next, l1))
        else:
            return ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
