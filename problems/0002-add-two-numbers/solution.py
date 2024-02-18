# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        result = dummy
        dummy = result
        while l1 or l2 or carry != 0:
            _sum = 0
            if l1:
                _sum += l1.val
                l1 = l1.next
            if l2:
                _sum += l2.val
                l2 = l2.next
            _sum += carry
            newNode = ListNode(_sum % 10)
            result.next = newNode
            carry = _sum // 10
            result = newNode
        
        return dummy.next


