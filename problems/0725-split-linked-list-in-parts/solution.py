# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        def getLength(head):
            curr = head
            count = 0
            while curr:
                curr = curr.next
                count += 1
            return count

        length = getLength(head)
        width, remainder = divmod(length, k)

        result = []
        curr = head
        for i in range(k):
            head = curr
            for j in range(width + (i < remainder) - 1):
                if curr: curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
            result.append(head)
        return result

