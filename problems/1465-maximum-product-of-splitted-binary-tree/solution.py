# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtreeSums = set()

        def sum(root):
            if root == None:
                return 0
            result = sum(root.right) + sum(root.left) + root.val
            subtreeSums.add(result)
            return result
        
        total_sum = sum(root)
        ideal_mid = total_sum / 2
        closestToIdeal = 0
        for possibleSum in subtreeSums:
             if math.fabs(possibleSum - ideal_mid) < math.fabs(closestToIdeal - ideal_mid):
                closestToIdeal = possibleSum
        print(closestToIdeal)
        return (((total_sum - closestToIdeal) % (10**9 + 7))) * ((closestToIdeal % (10**9 + 7))) % (10**9 + 7)

