# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t == None:
            return ''
        if (t.left == None and t.right == None):
            return str(t.val)
        base_string = ''
        base_string += str(t.val)
        left_string = self.tree2str(t.left) if t.left != None else ''
        right_string = self.tree2str(t.right) if t.right != None else ''
        base_string += '(' + left_string + ')'
        base_string += '(' + right_string + ')' if t.right != None else ''
        return base_string
