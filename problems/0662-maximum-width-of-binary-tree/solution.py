# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = {}
        self.max_diff = 0
        def traversal(root, index, level, dic):
            if root is None:
                return 
            dic.setdefault(level, [index, index])
            dic[level][0] = min(dic[level][0], index)
            dic[level][1] = max(dic[level][1], index)
            self.max_diff = max(self.max_diff, dic[level][1] - dic[level][0])

            traversal(root.left, 2*index, level+1, dic)
            traversal(root.right, 2*index+1, level+1, dic)
        traversal(root, 0, 0, dic)
        return self.max_diff+1

                
