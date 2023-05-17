# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1

        pairs = {}
        curr = head
        for i in range(n):
            if i <= (n/2) - 1:
                pairs[i] = curr.val 
            else:
                pairs[n-1-i] += curr.val
            curr = curr.next
        return max(pairs.values())
