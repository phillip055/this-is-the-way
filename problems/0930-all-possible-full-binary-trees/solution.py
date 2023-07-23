# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]

        result = []
        for idx in range(1, n, 2):
            lefts = self.allPossibleFBT(idx)
            rights = self.allPossibleFBT(n-idx-1)

            for left in lefts:
                for right in rights:
                    node = TreeNode(0, left, right)
                    result.append(node)
        return result

