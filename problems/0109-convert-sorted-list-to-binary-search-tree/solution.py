# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        fast, slow, prev = head, head, None

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        if prev:
            prev.next = None
        
        tree = TreeNode(slow.val)
        tree.left = self.sortedListToBST(head)
        tree.right = self.sortedListToBST(slow.next)
        return tree

        
