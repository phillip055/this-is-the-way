# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        toExplore = [root]
        result = []
        reverse = 1
        while toExplore:
            temp = []
            for _ in range(len(toExplore)):
                node = toExplore.pop(0)
                if reverse == -1:
                    temp = [node.val] + temp
                else:
                    temp = temp + [node.val]
                if node.left:
                    toExplore.append(node.left)
                if node.right:
                    toExplore.append(node.right)
            result.append(temp)
            reverse *= -1
        return result
