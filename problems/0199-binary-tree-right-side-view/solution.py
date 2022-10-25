# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        toExplore = [root]
        result = []
        while toExplore:
            mostRightForThisLevel = None
            for i in range(len(toExplore)):
                node = toExplore.pop(0)
                mostRightForThisLevel = node.val
                if node.left:
                    toExplore.append(node.left)
                if node.right:
                    toExplore.append(node.right)
            result.append(mostRightForThisLevel)
        return result
            
            
