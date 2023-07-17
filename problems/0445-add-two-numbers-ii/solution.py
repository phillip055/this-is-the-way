# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_linked_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        l1 = reverse_linked_list(l1)
        l2 = reverse_linked_list(l2)

        carry = 0
        result = ListNode(0)
        dummy = result
        while l1 != None or l2 != None or carry:
            _sum = 0
            if l1:
                _sum += l1.val
                l1 = l1.next
            if l2:
                _sum += l2.val
                l2 = l2.next
            if carry:
                _sum += 1
            result.next = ListNode(_sum % 10)
            result = result.next
            carry = 1 if _sum >= 10 else 0
        return reverse_linked_list(dummy.next)

