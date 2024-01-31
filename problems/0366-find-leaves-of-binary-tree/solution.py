# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        at_height = defaultdict(list)
        def dfs(root):
            if not root:
                return 0
            l_length = dfs(root.left)
            r_length = dfs(root.right)
            result = 1 + max(r_length, l_length)
            at_height[result].append(root.val)
            return result
        
        dfs(root)
        print(at_height)
        return at_height.values()
        
