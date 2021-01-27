# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        slow = fast = head 
        while fast and fast.next: # Find mid point 
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast: 
            slow = slow.next # Skip midpoint if odd legnth 
        
        while slow:
            if slow.val != stack.pop(): # Compare right half to left half  
                return False
            slow = slow.next
        return True
