# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
#         nodesToExplore = [(root, 0, 0)]
#         result = defaultdict(list)
#         while len(nodesToExplore):
#             node, x, y = nodesToExplore.pop(0)
#             if not node:
#                 continue
#             result[y].append((node.val, y))
#             nodesToExplore.extend(
#                 [
#                     (node.left, x+1, y-1),
#                     (node.right, x+1, y+1)
#                 ]
#             )
#         res=[]
#         for x in sorted(result.keys()):
#             l1=result[x]
#             l1.sort(key=lambda x:(x[1],x[0]))
#             l2=[]
#             for x in l1:
#                 l2.append(x[0])
#             res.append(l2)
#         return res
        ans = []
        def dfs(root,r,c):
            if root:
                ans.append([r,c,root.val])
                dfs(root.left,r+1,c-1)
                dfs(root.right,r+1,c+1)
            return
        dfs(root,0,0)
        ans=sorted(ans,key=lambda x:(x[1],x[0],x[2]))
        d=defaultdict(list)
        for i,j,k in ans:
            d[j].append(k)
        l=[]
        for i in d.values():
            l.append(i)
        return l
            
        
