# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
        slow, fast = head, head
        
        
        has_cycle = False
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        
        curr = head
        visited = set()
        if has_cycle:
            while curr:
                if curr in visited:
                    return curr
                visited.add(curr)
                curr = curr.next
        return None
