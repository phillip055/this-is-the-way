# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

# class Solution:
#     count = 0
#     def __init__(self, head: Optional[ListNode]):
#         self.head = head
#         cursor = head
#         while cursor:
#             cursor = cursor.next
#             self.count += 1

#     def getRandom(self) -> int:
#         rand = random.randint(0,self.count-1)
#         cursor = self.head
#         for i in range(rand):
#             cursor = cursor.next
#         return cursor.val


class Solution:
    
    def __init__(self, head: Optional[ListNode]):
        self.stack = []
        while head:
            self.stack.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.stack[int(random.random() * len(self.stack))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
