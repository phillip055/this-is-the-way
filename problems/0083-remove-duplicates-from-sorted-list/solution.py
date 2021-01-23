# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (head == None):
            return None
        start_head = head
        end_head = head
        
        while(end_head.next != None):
            end_head = end_head.next
            if (start_head.val != end_head.val):
                start_head.next = end_head
                start_head = end_head
            else:
                start_head.next = None
            
        return head

